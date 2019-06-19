from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User, Group

from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db.models.signals import post_save, m2m_changed



# Create your models here.

##creating faculty##

def create_faculty(instance):
    if True:
        faculty, created = Faculty.objects.get_or_create(username=instance.username)
        if created:
            faculty.fname = instance.first_name
            faculty.lname = instance.last_name
            faculty.email = instance.email
            faculty.teacher = True
            faculty.save()

def create_faculty_profile(sender, instance, created, **kwargs):
    if instance.groups.filter(name="teacher").count():
        create_faculty(instance)

def create_faculty_profile_m2m(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add' and instance.groups.filter(name="teacher").count():
        create_faculty(instance)

post_save.connect(create_faculty_profile, sender=User)
m2m_changed.connect(create_faculty_profile_m2m, sender=User.groups.through)
##creating faculty##


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
        fuser = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
        altemail = models.EmailField(blank=True)
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

    def __str__(self):
        return f'{self.name} GradeLevel'

    @property
    def grade(self):
        return self.id


class FamilyAccessUser(User):
    """ A person who can log into the non-admin side and see the same view as a student,
    except that he/she cannot submit timecards.
    This proxy model allows non-superuser registrars to update family user accounts.
    """
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        super(FamilyAccessUser, self).save(*args, **kwargs)
        self.groups.add(Group.objects.get_or_create(name='family')[0])


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Cohort(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField('Student', blank=True, db_table="sis_studentcohort_students")
    primary = models.BooleanField(blank=True, help_text="If set true - all students in this cohort will have it set as primary!")

    def __unicode__(self):
        return unicode(self.name)

def after_cohort_m2m(sender, instance, action, reverse, model, pk_set, **kwargs):
    if instance.primary:
        for student in instance.students.all():
            # Should be a get, but somehow there are sometimes more than one! Not so good.
            student_cohort = student.studentcohort_set.filter(cohort__id=instance.id)[0]
            student_cohort.primary = True
            student_cohort.save()

m2m_changed.connect(after_cohort_m2m, sender=Cohort.students.through)

class PerCourseCohort(Cohort):
    course = models.ForeignKey('lgmsschedule.Course', on_delete=models.CASCADE)

class ClassYear(models.Model):
    """ Class year such as class of 2010.
    """
    year = IntegerRangeField(unique=True, min_value=1900, max_value=2200, help_text="Example 2014")
    full_name = models.CharField(max_length=255, help_text="Example Class of 2014", blank=True)
    def __str__(self):
        return str(self.full_name)

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = "Class of %s" % (self.year,)
        super(ClassYear, self).save(*args, **kwargs)



class ReasonLeft(models.Model):
    reason = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.reason)


class Student(models.Model):
        user_students = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
        year = models.ForeignKey(GradeLevel, blank=True, null=True, on_delete=models.CASCADE)
        lrn_no = models.CharField('Learners Number', default="", max_length=64, blank=True)
        grad_date = models.DateField(blank=True, null=True)
        sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True, null=True)
        bday = models.DateField(blank=True, null=True, verbose_name="Birth Date")
        year = models.ForeignKey(GradeLevel, blank=True, null=True, on_delete=models.SET_NULL)
        class_of_year = models.ForeignKey(ClassYear, blank=True, null=True, on_delete=models.CASCADE)
        date_dismissed = models.DateField(blank=True, null=True)
        reason_left = models.ForeignKey(ReasonLeft, blank=True, null=True, on_delete=models.CASCADE)
        unique_id = models.IntegerField(blank=True, null=True, unique=True, help_text="For integration with outside databases")
        parent_guardian = models.CharField(max_length=150, blank=True, editable=False)
        streetname = models.CharField(max_length=255, verbose_name="Street Name", blank=True, null=True)
        zip = models.CharField(max_length=10, blank=True, editable=False)
        parent_email = models.EmailField(blank=True, editable=False)
        siblings = models.ManyToManyField('Student', blank=True)
        cohorts = models.ManyToManyField(Cohort, through='StudentCohort', blank=True)
        cache_cohort = models.ForeignKey(Cohort, editable=False, blank=True, null=True, on_delete=models.SET_NULL, help_text="Cached primary cohort.", related_name="cache_cohorts")
        #individual_education_program = models.BooleanField(help_text="Individual Program")
        cache_gpa = models.DecimalField(editable=False, max_digits=5, decimal_places=2, blank=True, null=True)


        class Meta:
            permissions = (
                # ("view_student", "View student"),
                ("view_ssn_student", "View student lrn_no"),
                ("view_mentor_student", "View mentoring information student"),
                ("reports", "View reports"),
        )

        def __str__(self):
            return self.lname + ", " + self.fname


        @property
        def homeroom(self):
            """ Returns homeroom for student """
            from lgmsschedule.models import Course
            try:
                courses = self.course_set.filter(homeroom=True)
                homeroom = self.course_set.get( homeroom=True)
            except:
                return ""


        def get_disciplines(self, mps, action_name=None, count=True):
            """ Shortcut to look up discipline records
            mp: Marking Period
            action_name: Discipline action name
            count: Boolean - Just the count of them """
            if hasattr(mps,'db'): # More than one?
                if len(mps):
                    start_date = mps.order_by('start_date')[0].start_date
                    end_date = mps.order_by('-end_date')[0].end_date
                    disc = self.studentdiscipline_set.filter(date__range=(start_date,end_date))
                else:
                    disc = self.studentdiscipline_set.none()
            else:
                disc = self.studentdiscipline_set.filter(date__range=(mps.start_date,mps.end_date))
            if action_name:
                disc = disc.filter(action__name=action_name)
            if count:
                return disc.count()
            else:
                return disc


    # two underscores make it too private!
        def _calculate_grade_for_single_course(self, course, marking_period, date_report):
            #print '_c_g_f_s_c(',course, marking_period, date_report, ')'
            """ Separate from __calculate_grade_for_courses() to avoid code duplication in
            ecwsp.benchmark_grade.utility """
            if marking_period:
                grade = float(self.grade_set.get(course=course, override_final=False, marking_period=marking_period).get_grade())
                credit = float(course.credits) / float(course.marking_period.count())
            else:
                grade = float(course.get_final_grade(self, date_report=date_report))
                #grade = float(grade)
                credit = float(course.get_credits_earned(date_report=date_report))
            return grade, credit

        #benchmark grade importance 
        def __calculate_grade_for_courses(self, courses, marking_period=None, date_report=None):
            #print '__c_g_f_c(', courses, marking_period, date_report, ')'
            if "lgmsbenchmarkgrade" in settings.INSTALLED_APPS:
                from ecwsp.benchmark_grade.utility import benchmark_calculate_grade_for_courses
                return benchmark_calculate_grade_for_courses(self, courses, marking_period, date_report)

            gpa = float(0)
            credits = float(0)
            for course in courses.distinct():
                try:
                    grade, credit = self._calculate_grade_for_single_course(course, marking_period, date_report)
                    credits += credit
                    gpa += float(grade) * credit
                except:
                    pass
            #print 'credits: ', credits
            if credits > 0:
                gpa = Decimal(str(gpa/credits)).quantize(Decimal("0.01"), ROUND_HALF_UP)
            else:
                gpa = "N/A"
            return gpa


        def calculate_gpa(self, date_report=None):
            """ Calculate students gpa
            date_report: Date for calculation (which effects credit value) defaults to today
            Note: self is student object"""
            if date_report == None:
                date_report = date.today()
            courses = self.course_set.filter(graded=True, marking_period__show_reports=True).exclude(omitcoursegpa__student=self).exclude(marking_period__school_year__omityeargpa__student=self).distinct()
            return self.__calculate_grade_for_courses(courses, date_report=date_report)

        def calculate_gpa_year(self, year=None, date_report=None):
            """ Calculate students gpa for one year
            year: Defaults to active year.
            date_report: Date for calculation (which effects credit value) defaults to today """
            if not date_report:
                date_report = date.today()
            courses = self.course_set.filter(graded=True, marking_period__school_year=year)
            x = self.__calculate_grade_for_courses(courses, date_report=date_report)
            return x

        def calculate_gpa_mp(self, marking_period):
            """ Calculate students gpa for one marking periods
            mp: Marking Periods to calculate for."""
            courses = self.course_set.filter(graded=True, omitcoursegpa=None, marking_period=marking_period)
            return self.__calculate_grade_for_courses(courses, marking_period=marking_period)

        @property
        def gpa(self):
            """ returns current GPA including absolute latest grades """
            if not self.cache_gpa:
                gpa = self.calculate_gpa()
                if gpa == "N/A":
                    return gpa
                else:
                    self.cache_gpa = gpa
                    self.save()
            return self.cache_gpa






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

    def __str__(self):
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




#for subjects
class Subjects(models.Model):
        subjectname = models.CharField('Subject Name', blank=False, max_length=64)
        color = models.CharField(max_length=64, default="#00b35c")

        def __str__(self):
            return '%s' % (self.subjectname)

        def get_html_badge(self):
            name = escape(self.subjectname)
            color = escape(self.color)
            html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, subjectname)
            return mark_safe(html)

        class Meta:
            verbose_name_plural = 'Subjects Lists Information'



class StudentCohort(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    primary = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.primary:
            for cohort in StudentCohort.objects.filter(student=self.student).exclude(id=self.id):
                cohort.primary = False
                cohort.save()

        super(StudentCohort, self).save(*args, **kwargs)

        if self.primary:
            self.student.cache_cohort = self.cohort
            self.student.save()

    
#####








    