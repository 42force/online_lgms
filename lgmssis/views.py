from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView



def index(request):
    return render(request, 'lgmssis/index.html')


def courselist(request):
    return render(request, 'lgmssis/course-listing.html')
