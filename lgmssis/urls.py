from django.urls import path
#from lgmssis.views import MyView
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('courselist/', CourseListView.as_view()),

    #path('hello/', MyView.as_view(), name='my-view'),

]
