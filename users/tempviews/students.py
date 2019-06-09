from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView

#method decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

#to count and average quiz and exams
from django.db.models import Avg, Count

#for formset layout of info
from django.forms import inlineformset_factory

#for redirect or errors like 404 page
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse, reverse_lazy

from .. decorators import student_required


#forms to be imported for student forms to work
from .. forms import UserRegisterForm



def register_students(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user_form.cleaned_data.get('username')
            messages.success(request, f'Account has been created{ username }!')
            return redirect('users/students/studentsprofile.html')
    else:
        user_form = UserRegisterForm()
    return render(request, 'users/students/studentsregister.html', {'user_form' : user_form})


class StudentView(CreateView):
    pass


class StudentInfoView(ListView):
    pass


class StudentSubjectView(ListView):
    pass