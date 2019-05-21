from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views import generic

from .forms import ApplyForm, EnquireForm
from django.shortcuts import render, redirect


def indexpage(request):
    return render(request, 'lgmssis/index.html')


#this is for enquire form
def enquire_form(request):
    if request.method == "POST":
        form = EnquireForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request,'home')
    else:
        form = EnquireForm()
    return render(request, 'flatpages/contact.html', {'form' : form} )




def register(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            redirect('home')
        else:
            form = ApplyForm()
            return render(request,'flatpages/apply-online.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class Apply(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy ('login')
    template_name = 'registration/apply-online.html'
