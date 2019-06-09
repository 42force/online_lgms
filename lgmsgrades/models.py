from django.db import models

# Create your models here.

from lgmssis.models import Student


# #for grades marking
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    

