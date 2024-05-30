from django.db import models

# Create your models here.

from lgmssis.models import Student
from lgmsschedule.models import Course, MarkingPeriod


from decimal import Decimal, ROUND_HALF_UP

# #for grades marking


class GradeComment(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=500)

    def __unicode__(self):
        return unicode(self.id) + ": " + unicode(self.comment)

    class Meta:
        ordering = ('id',)
# class Grade(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)


## GETTING GRADES ######
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True,)
    marking_period = models.ForeignKey(MarkingPeriod, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    override_final = models.BooleanField(help_text="Override final grade for marking period instead of calculating it.", blank=True, null=True,)
    comment = models.CharField(max_length=500, blank=True)
    letter_grade_choices = (
            ("E", "Excellent"),
            ("VG", "Very Good"),
            ("G", "Good"),
            ("S", "Satisfactory"),
            ("F", "Fair"),
            ("NI", "Needs Improvement / Passed"),
            ("U", "Unsatisfactory / Failed"),
        )
    letter_grade = models.CharField(max_length=2, blank=True, null=True, help_text="Will override grade.", choices=letter_grade_choices)

    class Meta:
        unique_together = (("student", "course", "marking_period"),)
        permissions = (
            ("change_own_grade", "Change grades for own class"),
            ('change_own_final_grade','Change final YTD grades for own class'),
        )

    def display_grade(self):
        """ Returns full spelled out grade such as Fail, Pass, 60.05, B"""
        return self.get_grade(display=True)

    def set_grade(self, grade):
        """ set grade to decimal or letter
            if grade is less than 1 assume it's a percentage
            returns success (True or False)"""
        try:
            grade = Decimal(str(grade))
            if grade < 1:
                # assume grade is a percentage
                grade = grade * 100
            self.grade = grade
            self.letter_grade = None
            return True
        except:
            grade = str.upper(str(grade)).strip()
            if grade in dict(self.letter_grade_choices):
                self.letter_grade = grade
                self.grade = None
                return True
            elif grade in ('', None, 'None'):
                self.grade = None
                self.letter_grade = None
                return True
            return False

    def get_grade(self, letter=False, display=False, rounding=None, minimum=None):
        """
        letter: Does nothing?
        display: For letter grade - Return display name instead of abbreviation.
        rounding: Numeric - round to this many decimal places.
        minimum: Numeric - Minimum allowed grade. Will not return lower than this.
        Returns grade such as 90.03, P, or F
        """
        if self.letter_grade:
            if display:
                return self.get_letter_grade_display()
            else:
                return self.letter_grade
        elif self.grade:
            grade = self.grade
            if minimum:
                if grade < minimum:
                    grade = minimum
            if rounding != None:
                string = '%.' + str(rounding) + 'f'
                grade = string % float(str(grade))
            return grade
        else:
            return ""

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.grade and self.letter_grade != None:
            raise ValidationError('Cannot have both numeric and letter grade')

    def save(self, *args, **kwargs):
        super(Grade, self).save(*args, **kwargs)

        #cache student's GPA
        if self.grade and self.student:
            self.student.cache_gpa = self.student.calculate_gpa()
            if self.student.cache_gpa != "N/A":
                self.student.save()

    def __str__(self):
        return (self.get_grade(self))



    

