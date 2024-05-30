from django.db import models
# Create your models here.
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.conf import settings

#this is the lgms models app lists
from lgmssis.models import CountryOption, Subjects, Student
#from users.models import Faculty


# class UserManager(BaseUserManager):
#         pass

# class User(AbstractUser):
#     is_students = models.BooleanField(default=False)
#     is_teachers = models.BooleanField(default=False)
#     is_parents = models.BooleanField(default=False)
#     is_admins = models.BooleanField(default=False)

# @property
# def is_students(self):
#         return self.is_students

# @property
# def is_teachers(self):
#         return self.is_teachers


# @property
# def is_parents(self):
#         return self.is_parents

# @property
# def is_admins(self):
#         return self.is_admins


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
        dateapply = models.DateField('Date of Application', default=date.today, editable=True)
        def __str__(self):
                return f'{self.fname}'
        
#this might be related on the instance being called
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics' )
    bio = models.TextField(max_length=500, blank=True)
    #role_group = models.OneToOneField(Group, on_delete=models.CASCADE, blank=True,null=True, related_name='user_role_group')


    def __str__(self):
        return f'{self.user} Profile!'




# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# class StudentProfile(models.Model):
#     user_student = models.OneToOneField(User, on_delete=models.CASCADE)
#     image_student = models.ImageField(default='default.jpg', upload_to='profile_pics_student')
#     lrn_no = models.CharField('Learners Number', default="", max_length=64, blank=True)
#     country_of_birth = models.ForeignKey(CountryOption, blank=True, null=True, on_delete=models.CASCADE)
#     birth_date = models.DateField('Date of Birth', default=date.today, editable=True)

#     @property
#     def age(self):
#         return int((datetime.now().date() - self.birth_date).days / 365.25)


#     def __str__(self):
#         return f'{self.user_student} Profile!'

# @receiver(post_save, sender=User)
# def create_user_studentprofile(sender, instance, created, **kwargs):
#     if created:
#         StudentProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_studentprofile(sender, instance, **kwargs):
#     instance.studentprofile.save()


# class ParentsProfile(models.Model):
#     user_parents = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio_parents = models.TextField(max_length=500, blank=True)
#     image_parents = models.ImageField(default='default.jpg', upload_to='profile_pics_parents')
#     streetname_parents = models.CharField(max_length=255, verbose_name="Street Name", blank=True, null=True)
#     cityname_parents = models.CharField(max_length=255, verbose_name="City Name", blank=True, null=True)
#     zip_parents = models.IntegerField('Zip Code', blank=True, null=True)
#     country_of_birth_parents = models.ForeignKey(CountryOption, blank=True, null=True, on_delete=models.CASCADE)
#     mobilenumber_parents = PhoneNumberField('Mobile Number', help_text='MOBILE FORMAT : +639178888888', blank=True)
#     birth_date_parents = models.DateField('Date of Birth', default=date.today, editable=True)


#     def __str__(self):
#         return f'{self.user_parents} Profile!'


# # @receiver(post_save, sender=User)
# # def create_user_parentsprofile(sender, instance, created, **kwargs):
# #     if created:
# #         ParentsProfile.objects.create(user=instance)

# # @receiver(post_save, sender=User)
# # def save_user_parentsprofile(sender, instance, **kwargs):
# #     instance.parentsprofile.save()


# class TeachersProfile(models.Model):
#     user_teachers = models.OneToOneField(User, on_delete=models.CASCADE)
#     image_teachers = models.ImageField(default='default.jpg', upload_to='profile_pics_teachers')
#     faculty_id = models.IntegerField('Faculty ID No.', default="1234")
#     bio_teachers = models.TextField(max_length=500, blank=True)

    
#     def __str__(self):
#         return f'{self.user_teachers} Profile!'

# # @receiver(post_save, sender=User)
# # def create_user_teachersprofile(sender, instance, created, **kwargs):
# #     if created:
# #         TeachersProfile.objects.create(user=instance)

# # @receiver(post_save, sender=User)
# # def save_user_teachersprofile(sender, instance, **kwargs):
# #     instance.parentsprofile.save()















