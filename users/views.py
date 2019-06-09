from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#this is for authentication per user only.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .forms import ( UserRegisterForm, 
                    UserUpdateForm, 
                    ProfileUpdateForm, 
                    ApplicationForm 
)

from django.views.generic import ListView, DetailView, CreateView
from django.db import transaction
from django.core.mail import EmailMessage
from django.contrib.auth.models import Group
#for email

from django.core.mail import send_mail
from django.conf import settings

#for the method decorator
from . decorators import student_required, teacher_required, parent_required

# from django.contrib.auth import get_user_model

# User = get_user_model()

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
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

###########this is where we test####################




@login_required
def test_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user = profile_form.save()
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


    #####################

def testregister(request):
    if request.method == 'POST':
        sform = UserRegisterForm(request.POST)
        sgroupform = GroupUpdateForm(request.POST)
        if sform.is_valid():
            sform.save()
            susername = sform.cleaned_data.get('username')
            messages.success(request, f'Account has been created{username}!')
            return redirect('home')
    else:
        sform = UserRegisterForm()
    return render(request, 'users/testregister.html', {'sform' : sform})

def register_example(request):
    
    return render(request, 'users/students/studentsregister.html')




################################################################

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                request.FILES, 
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/welcomehome.html', context)

##############################################################



###########this is where we test the register####################

# #hwat is the difference of this....?????
# def register_students(request):
#     if request.method == 'POST':
#         suser_form = UserRegisterForm(request.POST)
#         if suser_form.is_valid():
#             suser_form.save()
#             username = suser_form.cleaned_data.get('username')
#             messages.success(request, f'Account has been created {username} !')
#             return redirect('students_profile')
#     else:
#         suser_form = UserRegisterForm()
#     return render(request, 'users/students/studentsregister.html', {'suser_form' : suser_form})


# def register_teachers(request):
#     if request.method == 'POST':
#         tform = UserRegisterForm(request.POST)
#         if tform.is_valid():
#             tuser = tform.save()
#             tusername = tform.cleaned_data.get('username')
#             messages.success(request, f'Account has been created{tusername}!')
#             return redirect('users/teachers/teachersprofile')
#     else:
#         tform = UserRegisterForm()
#     return render(request, 'users/teachers/teachersregister.html', {'tform' : tform})


# # def register_parents(request):
# #     if request.method == 'POST':
# #         pform = UserRegisterForm(request.POST)
# #         if pform.is_valid():
# #             puser = pform.save()
# #             pusername = pform.cleaned_data.get('username')
# #             messages.success(request, f'Account has been created{pusername}!')
# #             return redirect('users/parents/parentsprofile.html')
# #     else:
# #         pform = UserRegisterForm()
# #     return render(request, 'users/parents/parentsregister.html', {'pform' : pform})


# # ##for teachers profile update
# # #for teacher

# # def teachers_profile(request):
# #     if request.method == 'POST':
# #         tuser_form = UserUpdateForm(request.POST, instance=request.user)
# #         tprofile_form = TeachersUpdateForm(request.POST, 
# #                                     request.FILES, 
# #                                     instance=request.user_teachers)
# #         if tuser_form.is_valid() and tprofile_form.is_valid():
# #             tuser_form.save()
# #             tprofile_form.save()
# #             messages.success(request, f'Account has been updated!')
# #             return redirect('users/teachers/teachersprofile')
# #         else:
# #             messages.error(request, f'Please correct the error below!')
# #     else:
# #         tuser_form = UserUpdateForm(instance=request.user)
# #         tprofile_form = TeachersUpdateForm(instance=request.user_teachers)

# #     context = {
# #         'tuser_form' : tuser_form,
# #         'tprofile_form' : tprofile_form
# #     }

# #     return render(request, 'users/teachers/teachersprofile.html', context)


# # def parents_profile(request):
# #     if request.method == 'POST':
# #         puser_form = UserUpdateForm(request.POST, instance=request.user)
# #         pprofile_form = ParentsUpdateForm(request.POST, 
# #                                     request.FILES, 
# #                                     instance=request.user_parents)
# #         if puser_form.is_valid() and pprofile_form.is_valid():
# #             puser_form.save()
# #             pprofile_form.save()
# #             messages.success(request, f'Account has been updated!')
# #             return redirect('parents_profile')
# #         else:
# #             messages.error(request, f'Please correct the error below!')
# #     else:
# #         tuser_form = UserUpdateForm(instance=request.user)
# #         tprofile_form = TeachersUpdateForm(instance=request.user)

# #     context = {
# #         'puser_form' : puser_form,
# #         'pprofile_form' : pprofile_form
# #     }

# #     return render(request, 'users/teachers/teachersprofile.html', context)


# # #### parents profile ###
# # @login_required
# # def students_profile(request):
# #     if request.method == 'POST':
# #         suser_form = UserUpdateForm(request.POST, instance=request.user)
# #         sprofile_form = StudentProfileUpdateForm(request.POST, 
# #                                     request.FILES, 
# #                                     instance=request.user)
# #         if suser_form.is_valid() and sprofile_form.is_valid():
# #             suser_form.save()
# #             sprofile_form.save()
# #             messages.success(request, f'Account has been updated!')
# #             return redirect('users/students/studentsprofile.html')
# #         else:
# #             messages.error(request, f'Please correct the error below!')
# #     else:
# #         suser_form = UserUpdateForm(instance=request.user)
# #         sprofile_form = StudentProfileUpdateForm(instance=request.user)

# #     context = {
# #         'suser_form' : suser_form,
# #         'sprofile_form' : sprofile_form
# #     }

# #     return render(request, 'users/students/studentsprofile.html', context)


# ##





