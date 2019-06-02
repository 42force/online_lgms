from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User, Group

from datetime import date

# Create your models here.

class CountryOption(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)
    
    class Meta:
        verbose_name_plural = 'Country Options List'




class Applicant(models.Model):
    fname = models.CharField(max_length=255, verbose_name="First Name", blank=True, null=True)
    lname = models.CharField(max_length=255, verbose_name="Last Name", blank=True, null=True)
    streetname = models.CharField(max_length=255, verbose_name="Street Name", blank=True, null=True)
    cityname = models.CharField(max_length=255, verbose_name="City Name", blank=True, null=True)
    zip = models.IntegerField('Zip Code', blank=True, null=True)
    country_of_birth = models.ForeignKey(CountryOption, blank=True, null=True, on_delete=models.CASCADE)
    mobilenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    programtype = {('CASA', 'CASA'),
        ('SPED', 'SPED'),
        ('GRADE SCHOOL', 'GRADE SCHOOL'),
        ('HIGH SCHOOL', 'HIGH SCHOOL'),
        ('HOMESTUDY', 'HOMESTUDY'),
        ('SPED', 'SPED')
    }

    progoption = models.CharField(max_length=20, choices=programtype, blank=True, default='CASA', help_text="Please select Program")


    heardoption = {('FACEBOOK', 'FACEBOOK'),
    ('FRIENDS', 'FRIENDS'),
    ('RADIO', 'RADIO'),
    ('NEWS', 'NEWS')}
    
    howdidyouhear = models.CharField(max_length=20, choices=programtype, blank=True, default='FACEBOOK', help_text="How did you hear about us?")
    graddate = models.DateField(auto_now=True)



class Enquire(models.Model):
    fullname =  models.CharField(max_length=255, verbose_name="Complete Name", blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobilenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True, null=True)
    place = models.CharField(max_length=255, verbose_name="Place or City", blank=True, null=True)
    programme = models.CharField(max_length=255, verbose_name="Course or Programme", blank=True, null=True)



class Faculty(models.Model):
        faculty_user = models.ForeignKey(User, on_delete=models.CASCADE)
        alt_email = models.EmailField(blank=True)
        number = models.IntegerField(blank=True)
        ext = models.CharField(max_length=10, blank=True, null=True)
        teacher = models.BooleanField()

        class Meta:
                verbose_name_plural = "Faculty"
                #ordering = ("first_name", "last_name")

        def save(self, *args, **kwargs):
                if Student.objects.filter(id=self.id).count():
                        raise ValidationError('Cannot have someone be a student AND faculty!')
                        super(Faculty, self).save(*args, **kwargs)
                        user, created = User.objects.get_or_create(username=self.username)
                if created:
                        user.password = "!"
                        user.save()
                        group, created = Group.objects.get_or_create(name="faculty")
                if created: group.save()
                user.groups.add(group)
                user.save()

        def full_clean(self, *args, **kwargs):
                """ Check if a Faculty exists, can't have someone be a Student and Faculty """
                if Student.objects.filter(id=self.id).count():
                        raise ValidationError('Cannot have someone be a student AND faculty!')
                super(Faculty, self).full_clean(*args, **kwargs)

class GradeLevel(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, verbose_name="Grade")
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return f'{self.name} GradeLevel'

    @property
    def grade(self):
        return self.id


class Student(models.Model):
        user_student = models.ForeignKey(User, on_delete=models.CASCADE )
        sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True, null=True)
        bday = models.DateField(blank=True, null=True, verbose_name="Birth Date")
        year = models.ForeignKey(GradeLevel, blank=True, null=True, on_delete=models.CASCADE)
        unique_id = models.IntegerField(blank=True, null=True, unique=True, help_text="For LEARNING NO")


class StudentFile(models.Model):
    file = models.FileField(upload_to="student_files")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class StudentHealthRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    record = models.TextField()



class SchoolYear(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    grad_date = models.DateField(blank=True, null=True)
    active_year = models.BooleanField(
        help_text="DANGER!! This is the current school year. There can only be one and setting this will remove it from other years. " \
                  "If you want to change the active year you almost certainly want to click Admin, Change School Year.")

#i removed this first to check if lambda error will still exist
    # benchmark_grade = models.BooleanField(default=lambda: str(Configuration.get_or_default("Benchmark-based grading", "False").value).lower() == "true",
    #                                       help_text="The configuration option \"Benchmark-based grading\" sets the default for this field")

    class Meta:
        ordering = ('-start_date',)

    def __unicode__(self):
        return self.name

    def get_number_days(self, date=date.today()):
        """ Returns number of active school days in this year, based on
        each marking period of the year.
        date: Defaults to today, date to count towards. Used to get days up to a certain date"""
        mps = self.markingperiod_set.filter(show_reports=True).order_by('start_date')
        day = 0
        for mp in mps:
            day += mp.get_number_days(date)
        return day

    def save(self, *args, **kwargs):
        super(SchoolYear, self).save(*args, **kwargs)
        if self.active_year:
            all = SchoolYear.objects.exclude(id=self.id).update(active_year=False)



class Cohort(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField('Student', blank=True, db_table="sis_studentcohort_students")
    primary = models.BooleanField(blank=True, help_text="If set true - all students in this cohort will have it set as primary!")

    def __unicode__(self):
        return unicode(self.name)


#created a model for Students

#class UserRegistration(models.Model):

    








    