from django.urls import path
#from lgmssis.views import MyView
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='course-listing.html'), name='course'),


    #path('hello/', MyView.as_view(), name='my-view'),

]
