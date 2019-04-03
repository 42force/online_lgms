from django.http import HttpResponse
from django.views import View
from django.shortcuts import render



def index(request):
    return render(request, 'lgmssis/index.html')
