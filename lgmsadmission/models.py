from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class ContactUs(models.Model):
    firstname = models.CharField('First Name', max_length=64)
    lastname = models.CharField('Last Name', max_length=64)
    inquryname = models.TextField('How can we help?',max_length=500, blank=True)
    phonenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
    email = models.EmailField('Email Address',unique=True, null=True, blank=True)

    def __str__(self):
                return f'{self.inquryname}'
        


    


