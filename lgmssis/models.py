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
    pass
    # fname = models.CharField(max_length=255, verbose_name="First Name")
    # lname = models.CharField(max_length=255, verbose_name="Last Name")
    # streetname = models.CharField(max_length=255, verbose_name="Street Name")
    # cityname = models.CharField(max_length=255, verbose_name="City Name")
    # zip = models.IntegerField('Zip Code', blank=True, null=True)
    # country_of_birth = models.ForeignKey(CountryOption, blank=True, null=True, on_delete=models.CASCADE)
    # mobilenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
 
    

