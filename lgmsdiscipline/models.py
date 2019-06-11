from django.db import models

# Create your models here.
from django.contrib.auth.models import User, Group
from django.conf import settings

from lgmssis.models import Student, Faculty


import datetime


class DisciplineAction(models.Model):
    name = models.CharField(max_length=255, unique=True)
    major_offense = models.BooleanField(
        help_text="This can be filtered by on Grade Analytics and other reports.")

    def __str__(self):
        return (self.name)


class DisciplineActionInstance(models.Model):
    action = models.ForeignKey(DisciplineAction, on_delete=models.CASCADE)
    student_discipline = models.ForeignKey('StudentDiscipline', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return (self.action) + " (" + (self.quantity) + ")"


class Infraction(models.Model):
    """ Infractions are things like  """
    comment = models.CharField(
        max_length=255,
        help_text='If comment is "Case note" these infractions will not be counted as a discipline issue in reports')

    def __str__(self):
        if len(self.comment) < 42:
            return self.comment
        else:
            return (self.comment[:42]) + ".."

    def all_actions(self):
        ordering = ('comment',)


class StudentDiscipline(models.Model):
    students = models.ManyToManyField(Student, limit_choices_to={'inactive': False})
    date = models.DateField(default=datetime.datetime.today)
    infraction = models.ForeignKey(Infraction, blank=True, null=True, on_delete=models.CASCADE)
    action = models.ManyToManyField(DisciplineAction, through='DisciplineActionInstance')
    comments = models.TextField(blank=True)
    private_note = models.TextField(blank=True)
    teacher = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.CASCADE)

    def show_students(self):
        if self.students.count() == 1:
            return self.students.all()[0]
        elif self.students.count() > 1:
            return "Multiple students"
        else:
            return None

    def comment_Brief(self):
        return self.comments[:100]

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        if self.students.count() == 1:
            stu = self.students.all()[0]
            return unicode(stu) + " " + unicode(self.date)
        return "Multiple Students " + unicode(self.date)

    def all_actions(self):
        action = ""
        for a in self.disciplineactioninstance_set.all():
            action += unicode(a) + " "
        return action

    def get_active(self):
        """Returns all active discipline records for the school year.
        If schedule is not installed it returns all records
        Does not return case notes"""
        try:
            school_start = SchoolYear.objects.get(active_year=True).start_date
            school_end = SchoolYear.objects.get(active_year=True).end_date
            case_note = PresetComment.objects.get(comment="Case note")
            return StudentDiscipline.objects.filter(date__range=(school_start, school_end)).exclude(infraction=case_note)
        except:
            case_note = PresetComment.objects.get(comment="Case note")
            return StudentDiscipline.objects.all().exclude(infraction=case_note)