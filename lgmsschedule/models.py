from django.db import models

from django.db.models import Max
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, Group

from lgmssis.models import Student, SchoolYear, GradeLevel, Faculty

#need to understand this
from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
import copy

# Create your models here.


class MarkingPeriod(models.Model):
    name = models.CharField(max_length=255, unique=True,)
    shortname = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    active = models.BooleanField(help_text="Teachers may only enter grades for active marking periods. There may be more than one active marking period.")
    show_reports = models.BooleanField(default=True, help_text="If checked this marking period will show up on reports.")
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    school_days = models.IntegerField(blank=True, null=True, help_text="If set, this will be the number of days school is in session. If unset, the value is calculated by the days off.")

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return str(self.name)
    
    def clean(self):
        from django.core.exceptions import ValidationError
        # Don't allow draft entries to have a pub_date.
        if self.start_date > self.end_date:
            raise ValidationError('Cannot end before starting!')

    def get_number_days(self, date=date.today()):
        """ Get number of days in a marking period"""
        if (self.school_days or self.school_days == 0) and date >= self.end_date:
            return self.school_days
        day = 0
        current_day = self.start_date
        while current_day <= date:
            is_day = False
            if current_day >= self.start_date and current_day <= self.end_date:
                days_off = []
                for d in self.daysoff_set.all().values_list('date'): days_off.append(d[0])
                if not current_day in days_off:
                    if self.monday and current_day.isoweekday() == 1:
                        is_day = True
                    elif self.tuesday and current_day.isoweekday() == 2:
                        is_day = True
                    elif self.wednesday and current_day.isoweekday() == 3:
                        is_day = True
                    elif self.thursday and current_day.isoweekday() == 4:
                        is_day = True
                    elif self.friday and current_day.isoweekday() == 5:
                        is_day = True
                    elif self.saturday and current_day.isoweekday() == 6:
                        is_day = True
                    elif self.sunday and current_day.isoweekday() == 7:
                        is_day = True
            if is_day: day += 1
            current_day += timedelta(days=1)
        return day


class DaysOff(models.Model):
    date = models.DateField()
    marking_period = models.ForeignKey(MarkingPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

class Period(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ('start_time',)

    def __str__(self):
        return "%s %s-%s" % (self.name, self.start_time.strftime('%I:%M%p'), self.end_time.strftime('%I:%M%p'))


class CourseMeet(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    day_choice = (   # ISOWEEKDAY
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
        
    )
    day = models.CharField(max_length=1, choices=day_choice)
    location = models.ForeignKey('Location', blank=True, null=True, on_delete=models.CASCADE)


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class CourseEnrollment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default="Student", blank=True)
    attendance_note = models.CharField(max_length=255, blank=True, help_text="This note will appear when taking attendance")
    year = models.ForeignKey(GradeLevel, blank=True, null=True, on_delete=models.CASCADE)
    exclude_days = models.ManyToManyField('Day', blank=True, \
        help_text="Student does not need to attend on this day. Note courses already specify meeting days, this field is for students who have a special reason to be away")

    class Meta:
        unique_together = (("course", "user", "role"),)

    def save(self, *args, **kwargs):
        if not self.id and hasattr(self.user, 'student'):
            student = self.user.student
            #Asp has been depreciated
            #from ecwsp.sis.models import ASPHistory
            #asp = ASPHistory(student=student, asp=self.course.shortname, enroll=True)
            #asp.save()
        super(CourseEnrollment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if hasattr(self.user, 'student'):
            student = self.user.student
        super(CourseEnrollment, self).delete(*args, **kwargs)

class Day(models.Model):
    dayOfWeek = (
        ("1", 'Monday'),
        ("2", 'Tuesday'),
        ("3", 'Wednesday'),
        ("4", 'Thursday'),
        ("5", 'Friday'),
        ("6", 'Saturday'),
        ("7", 'Sunday'),
    )
    day = models.CharField(max_length=1, choices=dayOfWeek)
    def __unicode__(self):
        return self.get_day_display()
    class Meta:
        ordering = ('day',)


        #skip department grade##

#course is similar to subject but more of casa course, junior high, senior high, special education
class Course(models.Model):
    active = models.BooleanField(default=True, help_text="If active, course will show in Moodle.")
    fullname = models.CharField(max_length=255, unique=True)
    shortname = models.CharField(max_length=255)
    marking_period = models.ManyToManyField(MarkingPeriod, blank=True)
    periods = models.ManyToManyField(Period, blank=True, through=CourseMeet)
    teacher = models.ForeignKey(Faculty, blank=True, null=True, related_name="ateacher", on_delete=models.CASCADE)
    secondary_teachers = models.ManyToManyField(Faculty, blank=True, related_name="secondary_teachers")
    homeroom = models.BooleanField(help_text="Homerooms can be used for attendance")
    graded = models.BooleanField(default=True, help_text="Teachers can submit grades for this course")
    enrollments = models.ManyToManyField(User, through=CourseEnrollment, blank=True)
    description = models.TextField(blank=True)
    #credits = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Credits effect gpa.")
    #department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)
    level = models.ForeignKey(GradeLevel, blank=True, null=True, on_delete=models.CASCADE)
    last_grade_submission = models.DateTimeField(blank=True, null=True, editable=False)

    def __unicode__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)
        # assign teacher in as enrolled user
        try:
            if self.teacher:
                enroll, created = CourseEnrollment.objects.get_or_create(course=self, user=self.teacher, role="teacher")
        except: pass

    def grades_link(self):
       link = '<a href="/lgmsgrades/teacher_grade/upload/%s" class="historylink"> Grades </a>' % (self.id,)
       return link
    grades_link.allow_tags = True



class Award(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return unicode(self.name)

class AwardStudent(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marking_period = models.ForeignKey(MarkingPeriod, blank=True, null=True, on_delete=models.CASCADE)


