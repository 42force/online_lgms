from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.urls import reverse

#from django.core import urlresolvers
#from django.core import urlresolvers
from django.contrib.auth.models import User

from . models import StudentDiscipline
from lgmssis.models import SchoolYear
#from ecwsp.administration.models import *
from lgmssis.lookups import StudentLookup


class StudentWithDisciplineLookup(StudentLookup):
    def format_item(self,student):
        year = student.year
        if not year: year = "Unknown year"
        image = student.pic.url_70x65
        if not image: image = "/static/images/noimage.jpg"
        school_start = SchoolYear.objects.get(active_year=True).start_date
        school_end = SchoolYear.objects.get(active_year=True).end_date
        priors = StudentDiscipline.objects.filter(students=student).filter(date__range=(school_start, school_end))
        output = "<table style=\"border-collapse: collapse; width:700px;\"><tr><td><img src=%s></td><td>%s %s <br/><a href=\"/sis/disc/report/%s\">View full report</a>" \
            % (image, student.first_name, student.last_name, student.id)
        for prior in priors:
            output += "<br/>%s - %s - %s - %s" % (prior.date.strftime('%b %d, %Y'), prior.infraction, prior.all_actions(), prior.comments)
        output += "</td></tr></table>"
        return output

    def get_objects(self,ids):
        return Student.objects.filter(pk__in=ids).order_by('lname')

