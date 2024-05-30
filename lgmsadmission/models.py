from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


import datetime

import django.utils.timezone

from datetime import date
from django.contrib.auth.models import User, Group


from lgmssis.models import Applicant, CountryOption, Subjects, Student


# Create your models here.

class AdmissionLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField(unique=True, help_text="Order in which level appears. 1 being first.")
    def __unicode__(self):
        return unicode(self.name)
    def edit(self):
        return "Edit"
    def show_checks(self):
        """Show checks needed for this level"""
        msg = '|'
        for check in self.admissioncheck_set.all():
            msg += "%s | " % (check.name,)
        return msg
    class Meta:
        ordering = ('order',)


class AdmissionCheck(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(AdmissionLevel, on_delete=models.CASCADE)
    required = models.BooleanField(
        default=True,
        help_text="When true, applicant cannot meet any level beyond this. When false, "\
                  "applicant can leapfrog check items.")
    class Meta:
        ordering = ('level','name')
    def __unicode__(self):
        return unicode(self.name)

class ApplicationDecisionOption(models.Model):
    name = models.CharField(max_length=255, unique=True)
    level = models.ManyToManyField(
        AdmissionLevel,
        blank=True,
        help_text="This decision can apply for these levels.")
    def __unicode__(self):
        return unicode(self.name)


class WithdrawnChoices(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return unicode(self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Withdrawn Choices"

class ContactUs(models.Model):
    firstname = models.CharField('First Name', max_length=64)
    lastname = models.CharField('Last Name', max_length=64)
    inquryname = models.TextField('How can we help?',max_length=5000, blank=True)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    datecontact = models.DateField('Date of Contact', default=date.today, editable=False)

    def __str__(self):
                return f'{self.inquryname}'

    class Meta:
         verbose_name_plural = "Contact Us Lists"




class Inquiry(models.Model):
    firstname = models.CharField('Name', max_length=64)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    programme = models.CharField(max_length=255, verbose_name="Course or Programme", blank=True, null=True)
    #date = models.DateField()
    dateinquiry = models.DateField('Date of Inquiry', default=date.today, editable=False)
    def __str__(self):
                return f'{self.firstname}'

    class Meta:
         verbose_name_plural = "Inquiry Lists"


class CasaInquiry(models.Model):
    firstname = models.CharField('Name', max_length=64)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    programme = models.CharField(max_length=255, verbose_name="Casa Inquiry", blank=True, null=True, help_text='CASA programme')
    inquiryname = models.TextField('How can we help?',max_length=350, blank=True)
    datecasainquiry = models.DateField('Date of  CASA Inquiry', default=date.today, editable=False)

    def __str__(self):
                return f'{self.firstname}'

    class Meta:
         verbose_name_plural = "CASA Inquiry Lists"


class GradeSchoolInquiry(models.Model):
    firstname = models.CharField('Name', max_length=64)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    programme = models.CharField(max_length=255, verbose_name="Grade School  programme", blank=True, null=True, help_text='Grade School programme')
    inquiryname = models.TextField('How can we help?',max_length=350, blank=True)
    dategsinquiry = models.DateField('Date of GS Inquiry', default=date.today, editable=False)

    def __str__(self):
                return f'{self.firstname}'

    class Meta:
         verbose_name_plural = "GS Inquiry Lists"


class HighSchoolInquiry(models.Model):
    firstname = models.CharField('Name', max_length=64)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    programme = models.CharField(max_length=255, verbose_name="High School  programme", blank=True, null=True, help_text='High School programme')
    inquiryname = models.TextField('How can we help?',max_length=350, blank=True)
    dategsinquiry = models.DateField('Date of HS Inquiry', default=date.today, editable=False)

    def __str__(self):
                return f'{self.firstname}'

    class Meta:
         verbose_name_plural = "HS Inquiry Lists"


class HomeStudyInquiry(models.Model):
    firstname = models.CharField('Name', max_length=64)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    programme = models.CharField(max_length=255, verbose_name="Home Study programme", blank=True, null=True, help_text='Home Study programme')
    inquiryname = models.TextField('How can we help?',max_length=350, blank=True)
    datehomeinquiry = models.DateField('Date of HOMEStudy Inquiry', default=date.today, editable=False)

    def __str__(self):
                return f'{self.firstname}'

    class Meta:
         verbose_name_plural = "Home Study Programme Inquiry Lists"


class SpedInquiry(models.Model):
    firstname = models.CharField('Name', max_length=64)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    programme = models.CharField(max_length=255, verbose_name="SPED programme", blank=True, null=True, help_text='SPED programme')
    inquiryname = models.TextField('How can we help?',max_length=350, blank=True)
    datespedinquiry = models.DateField('Date of SPED Inquiry', default=date.today, editable=False)

    def __str__(self):
                return f'{self.firstname}'

    class Meta:
         verbose_name_plural = "SPED Inquiry Lists"




class ApplicantStandardTestResult(models.Model):
    """ Standardized test instance. This is the results of a student taking a test """
    date = models.DateField('Date of Application', default=date.today)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    test = models.ForeignKey('lgmsexam.StandardTest', on_delete=models.CASCADE)
    show_on_reports = models.BooleanField(default=True, help_text="If true, show this test result on a report such as a transcript. " + \
        "Note entire test types can be marked as shown on report or not. This is useful if you have a test that is usually shown, but have a few instances where you don't want it to show.")

    class Meta:
        unique_together = ('date', 'applicant', 'test')

    def __unicode__(self):
        try:
            return '%s %s %s' % (unicode(self.applicant), unicode(self.test), self.date)
        except:
            return "Standard Test Result"

    @property
    def total(self):
        """Returns total for the test instance
        This may be calculated or marked as "is_total" on the category
        """
        if self.test.calculate_total:
            total = 0
            for cat in self.standardcategorygrade_set.all():
                total += cat.grade
            return str(total).rstrip('0').rstrip('.')
        elif self.standardcategorygrade_set.filter(category__is_total=True):
            totals = self.standardcategorygrade_set.filter(category__is_total=True)
            if totals:
                return str(totals[0].grade).rstrip('0').rstrip('.')
        else:
            return 'N/A'

class ApplicantStandardCategoryGrade(models.Model):
    """ Grade for a category and result """
    category = models.ForeignKey('lgmsexam.StandardCategory', on_delete=models.CASCADE)
    result = models.ForeignKey(ApplicantStandardTestResult, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=6,decimal_places=2)




class CasaApplication(models.Model):

        seshoption = {('7:30', '7:30 Class'),
        ('10:30', '10:30 Class'),
        ('1:30', '1:30 Class')}

        STATE_CHOICES = (
        (True, u'Yes'),
        (False, u'No'),
        )
        #forms.CharField(widget=forms.Select(choices=CHOICES))
        sessionchoice = models.CharField(verbose_name="Choose Class", default='7:30 CLASS', max_length=65)
        #sessionchoice = forms.Select(choices=seshoption)
        fname = models.CharField(max_length=255, verbose_name="First Name", blank=True, null=True)
        lname = models.CharField(max_length=255, verbose_name="Last Name", blank=True, null=True)
        bday = models.DateField(blank=True, null=True, verbose_name="Birth Date")
        pic = models.ImageField(upload_to="applicant_pics",blank=True, null=True)
        streetname = models.CharField(max_length=255, verbose_name="Address", blank=True, null=True)
        cityname = models.CharField(max_length=255, verbose_name="City Name", blank=True, null=True)
        #zip = models.IntegerField('Zip Code', blank=True, null=True)
        country_of_birth = models.ForeignKey(CountryOption, blank=True, null=True, on_delete=models.CASCADE)
        mobilenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
        parent_guardian_first_name = models.CharField(verbose_name="Parent or Guardians First Name", max_length=150, blank=True)
        parent_guardian_last_name = models.CharField(verbose_name="Parent or Guardians First Name", max_length=150, blank=True)
        parent_guardian_occupation = models.CharField(verbose_name="Parent or Guardians Occupation", max_length=150, blank=True)
        parent_guardian_company_firm = models.CharField(verbose_name="Parent or Guardians Company or Firm Name", max_length=150, blank=True)
        company_firm_address = models.CharField(verbose_name="Company or Business Name", max_length=150)
        company_firm_phone = PhoneNumberField('Company Office Number',help_text='Phone Format : +6327777777', blank=True)
        relationship_to_student = models.CharField(max_length=500, blank=True)
        email = models.EmailField(unique=True, null=True, blank=True)
        
        heardoption = {('FACEBOOK', 'FACEBOOK'),
        ('FRIENDS', 'FRIENDS'),
        ('RADIO', 'RADIO'),
        ('NEWS', 'NEWS')}
    
        howdidyouhear = models.CharField(verbose_name="How did you heard about us?",max_length=20, choices=heardoption, blank=True, default='FACEBOOK')
        date_added = models.DateField(auto_now_add=True, blank=True, null=True)

        level = models.ForeignKey(AdmissionLevel, blank=True, null=True, on_delete=models.SET_NULL)
        checklist = models.ManyToManyField(AdmissionCheck, blank=True)
        application_decision = models.ForeignKey(ApplicationDecisionOption, blank=True, on_delete=models.CASCADE)
        application_decision_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
        withdrawn = models.ForeignKey(WithdrawnChoices, blank=True, null=True, on_delete=models.CASCADE)
        withdrawn_note = models.CharField(max_length=500, blank=True)
        lgmssis_student = models.OneToOneField('lgmssis.Student', 
        blank=True,
        null=True,
        related_name="appl_student",
        on_delete=models.SET_NULL)

        name_of_children = models.CharField(verbose_name="Name of Other Children",max_length=150, blank=True )
        present_school = models.CharField(verbose_name="Name Of School", max_length=150, blank=True)
        present_school_address = models.CharField(verbose_name="Current School Address", max_length=150, blank=True)
        years_of_attend = models.IntegerField(verbose_name="Years of Attendance", unique=True, help_text="1 year" )
        
        reportcard = models.BooleanField(default=False, help_text="Report Card of current and preceeding years.", choices=STATE_CHOICES,)
        idphoto = models.BooleanField(default=True, help_text="2 pcs ID PHOTO.")
        birthcert = models.BooleanField(default=True, help_text="Birth Certificate Original or Xerox.")
        baptismalcert = models.BooleanField(default=True, help_text="Baptismal Certificate Original or Xerox.")
        letterrecom = models.BooleanField(default=True, help_text="Letter of Recommendatio, you may download or request.")
        passportphoto = models.BooleanField(default=True, help_text="passport sized photos 2pcs.")
        acrform = models.BooleanField(default=False, help_text="ACR For Foreign Applicants Only.")
        healthform = models.BooleanField(default=True, help_text="Health Form from LGMS.")
        
        def __str__(self):
                return f'{self.fname}'


class GradeSchoolApplication(models.Model):
    pass

class HighSchoolApplication(models.Model):
    pass



class Document(models.Model):
    description = models.CharField(help_text="Put your Description Notes e.g. ID, Passport, Birth Certificate and Please ZIP your files", max_length=255, blank=True)
    document = models.FileField(help_text="Please zip your file", upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

        

    