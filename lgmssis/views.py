from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


def indexpage(request):
    return render(request, 'lgmssis/index.html')
