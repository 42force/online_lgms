from django import forms
from django.contrib.auth.models import User, Group
from lgmssis.models import CountryOption
from django.contrib.auth.forms import UserCreationForm
from datetime import date

from .models import Profile, Application

#THIS IS WHERE WE MODIFY ADD FORMS TO USER

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User 
        fields  = ['username', 'email', 'password1', 'password2',]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.DateTimeField()
    class Meta:
        model = Profile
        fields = [ 'image', 'zip', 'bio', 'cityname', 'country_of_birth', 'user']


class TeachersUpdateForm(forms.ModelForm):
    pass


class ParentsUpdateForm(forms.ModelForm):
    pass 



class ApplicationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Application
        fields = ['fname', 'lname', 'mobilenumber', 'streetname', 'country_of_birth', 'progoption', 'howdidyouhear' ]

    


    
