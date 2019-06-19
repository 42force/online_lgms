from django.db.models import FileField
from django.db import models
from django.db.models import Sum
from django.db.models import signals
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.dispatch import dispatcher
from django.core.exceptions import ValidationError
from django.urls import reverse


from ckeditor.fields import RichTextField
from django.conf import settings
# Create your models here.


class Benchmark(models.Model):
    measurement_topics = models.ManyToManyField('MeasurementTopic')
    number = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=700)
    year = models.ForeignKey('lgmssis.GradeLevel', blank=True, null=True, on_delete=models.CASCADE)

    def display_measurement_topics(self):
        txt = ""
        for topic in self.measurement_topics.all():
            txt += unicode(topic) + ", "
        if txt:
            return txt[:-2]

    def __unicode__(self):
        return __str__('%s %s' % (self.number, self.name))

    class Meta:
        unique_together = ('number','name')
        ordering = ('number', 'name',)


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __unicode__(self):
        return self.name


class MeasurementTopic(models.Model):
    name = models.CharField(max_length=700)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)
    def __unicode__(self):
        if self.department:
            return __str__(self.department) + " - " + __str__(self.name)
        else:
            return __str__(self.name)
    class Meta:
        unique_together = ('name', 'department')
        ordering  = ('department','name')
