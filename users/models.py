from django.db import models
# Create your models here.
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.contrib.auth.models import AbstractUser

#this is the lgms models app lists
from lgmssis.models import CountryOption
#from users.models import Faculty


class Application(models.Model):

        fname = models.CharField(max_length=255, verbose_name="First Name", blank=True, null=True)
        lname = models.CharField(max_length=255, verbose_name="Last Name", blank=True, null=True)
        streetname = models.CharField(max_length=255, verbose_name="Street Name", blank=True, null=True)
        cityname = models.CharField(max_length=255, verbose_name="City Name", blank=True, null=True)
        zip = models.IntegerField('Zip Code', blank=True, null=True)
        country_of_birth = models.ForeignKey(CountryOption, blank=True, null=True, on_delete=models.CASCADE)
        mobilenumber = PhoneNumberField('Mobile Number',help_text='MOBILE FORMAT : +639178888888', blank=True)
        email = models.EmailField(unique=True, null=True, blank=True)
        programtype = {('CASA', 'CASA'),
                ('SPED', 'SPED'),
                ('GRADE SCHOOL', 'GRADE SCHOOL'),
                ('HIGH SCHOOL', 'HIGH SCHOOL'),
                ('HOMESTUDY', 'HOMESTUDY'),
                ('SPED', 'SPED')
        }

        progoption = models.CharField(verbose_name="Program Option", max_length=20, choices=programtype, blank=True, default='CASA', help_text="Please select Program")


        heardoption = {('FACEBOOK', 'FACEBOOK'),
        ('FRIENDS', 'FRIENDS'),
        ('RADIO', 'RADIO'),
        ('NEWS', 'NEWS')}
    
        howdidyouhear = models.CharField(verbose_name="How did you heard about us?",max_length=20, choices=heardoption, blank=True, default='FACEBOOK', help_text="How did you hear about us?")
        
        def __str__(self):
                return f'{self.fname}'
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics' )
    bio = models.TextField(max_length=500, blank=True)
    streetname = models.CharField(max_length=255, verbose_name="Street Name", blank=True, null=True)
    cityname = models.CharField(max_length=255, verbose_name="City Name", blank=True, null=True)
    zip = models.IntegerField('Zip Code', blank=True, null=True)
    country_of_birth = models.ForeignKey(CountryOption, blank=True, null=True, on_delete=models.CASCADE)
    mobilenumber = PhoneNumberField('Mobile Number', help_text='MOBILE FORMAT : +639178888888', blank=True)
    birth_date = models.DateField('Date of Birth', default=date.today, editable=True)
    role_group = models.OneToOneField(Group, on_delete=models.CASCADE, blank=True,null=True, related_name='user_role_group')


    def __str__(self):
        return f'{self.user} Profile!'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



