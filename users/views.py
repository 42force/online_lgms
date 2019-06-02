from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ApplicationForm
from django.db import transaction
from django.core.mail import EmailMessage
#for email

from django.core.mail import send_mail
from django.conf import settings

#from .forms import User ProfileForm,

# Create your views here.

def apply_online(request):
    if request.method == 'POST':
        app_form = ApplicationForm(request.POST)
        if app_form.is_valid():
            app_form.save()
            mail_subject = 'Thank you for your Application'
            message = 'Application Received, we will be in touch shortly'
            to_email = app_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    else:
        app_form = ApplicationForm()
    return render(request, 'users/applyonline.html', {'app_form' : app_form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created{username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Please correct the error below!')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }

    return render(request, 'users/studentsprofile.html', context)





def register_students(request):
    return render(request, 'users/students/studentsregister.html')


def register_teachers(request):
    pass

def register_parents(request):
    pass




        
        


