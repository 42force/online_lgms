from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class ContactUs(models.Model):
    firstname = models.CharField('First Name', max_length=64)
    lastname = models.CharField('Last Name', max_length=64)
    inquryname = models.TextField('How can we help?',max_length=5000, blank=True)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)

    def __str__(self):
                return f'{self.inquryname}'

    class Meta:
         verbose_name_plural = "Contact Us Lists"




class Inquiry(models.Model):
    firstname = models.CharField('Name', max_length=64)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)
    programme = models.CharField(max_length=255, verbose_name="Course or Programme", blank=True, null=True)
    date = models.DateField()
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

    def __str__(self):
                return f'{self.firstname}'

    class Meta:
         verbose_name_plural = "SPED Inquiry Lists"

        

    