from django.urls import path
#from lgmssis.views import MyView
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.courselist, name='courselist')


    #path('hello/', MyView.as_view(), name='my-view'),

]
