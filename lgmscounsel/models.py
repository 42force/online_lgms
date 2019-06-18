
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.urls import reverse


# from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.db import models
from ckeditor.fields import RichTextField
from lgmssis.models import Student
#from ecwsp.administration.models import Configuration
import datetime
import logging

# Create your models here.


class FollowUpAction(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return unicode(self.name)

class StudentMeetingCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __unicode__(self):
        return unicode(self.name)

class StudentMeeting(models.Model):
    students = models.ManyToManyField(Student)
    category = models.ForeignKey(StudentMeetingCategory,blank=True,null=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    notes = RichTextField(blank=True)
    follow_up_action = models.ForeignKey(FollowUpAction,blank=True,null=True, on_delete=models.CASCADE)
    follow_up_notes = models.CharField(max_length=2024,blank=True)
    reported_by = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to = {'groups__name': 'faculty'})
    #referral_form = models.ForeignKey('ReferralForm',blank=True, editable=False, on_delete=models.CASCADE)
    file = models.FileField(upload_to='student_meetings',blank=True,null=True)
    def __unicode__(self):
        students = ''
        for student in self.students.all():
            students += '%s, ' % (student,)
        return '%s meeting with %s' % (unicode(self.reported_by),students[:-2])
    def display_students(self):
        txt = ''
        for student in self.students.all():
            txt += '%s, ' % (student)
        return txt[:-2]

    class Meta:
        ordering = ('-date',)
