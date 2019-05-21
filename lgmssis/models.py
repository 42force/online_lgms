from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class CountryOption(models.Model):
    name = models.CharField('Country Options', max_length=500)

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
    email = models.EmailField(unique=True)

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

    graddate = models.DateField(blank=False)



class Enquire(models.Model):
    fullname =  models.CharField(max_length=255, verbose_name="Complete Name", blank=True, null=True)
    email = models.EmailField(unique=True)
    place = models.CharField(max_length=255, verbose_name="Place or City", blank=True, null=True)
    programme = models.CharField(max_length=255, verbose_name="Course or Programme", blank=True, null=True)











    