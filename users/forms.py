from django import forms
from django.contrib.auth.models import User, Group
from lgmssis.models import CountryOption
from django.contrib.auth.forms import UserCreationForm
from datetime import date


# from django.contrib.auth import get_user_model

# User = get_user_model()


from .models import Profile, Application

#THIS IS WHERE WE MODIFY ADD FORMS TO USER

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User 
        fields  = ['username', 'email', 'password1', 'password2',]


#this is for the profile update and change 
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.DateTimeField()
    class Meta:
        model = Profile
        fields = [ 'image',  'bio',  'user']
        

class ApplicationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Application
        fields = ['fname', 'lname', 'mobilenumber', 'streetname', 'country_of_birth', 'progoption', 'howdidyouhear' ]

    











# class TeachersUpdateForm(forms.ModelForm):
#     class Meta:
#         model = TeachersProfile
#         fields = ['image_teachers', 'faculty_id', 'bio_teachers']



# class ParentsUpdateForm(forms.ModelForm):
#     class Meta:
#         model = ParentsProfile
#         fields = ['image_parents', 'bio_parents', 'streetname_parents', 'cityname_parents', 'zip_parents', 'country_of_birth_parents', 'mobilenumber_parents', 'birth_date_parents']


# class StudentProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = StudentProfile
#         fields = ['user_student', 'image_student', 'birth_date', 'country_of_birth']



###for applicants information only before admission####
    
