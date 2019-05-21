from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.

class CountryOption(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return unicode(self.name)
    class Meta:
        ordering = ['name']


def get_default_country():
    return CountryOption.objects.get_or_create(name=settings.ADMISSIONS_DEFAULT_COUNTRY)


# class Applicant(models.Model):

#     fname = models.CharField(max_length=255, verbose_name="First Name")
#     lname = models.CharField(max_length=255, verbose_name="Last Name")
#     streetname = models.CharField(max_length=255, verbose_name="Street Name")
#     cityname = models.CharField(max_length=255, verbose_name="City Name")
#     zip = models.IntegerField('Zip Code', blank=True, null=Trues)
#     country_of_birth = models.ForeignKey(CountryOption, blank=True, null=True, default=get_default_country, on_delete=models.CASCADE)
#     mobilenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
 
    

