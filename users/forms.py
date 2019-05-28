from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#THIS IS WHERE WE MODIFY ADD FORMS TO USER

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User 
        fields  = ['username', 'email', 'password1', 'password2', 'is_staff']
