from django.urls import path
#from lgmssis.views import MyView

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('course_listing/', views.course_listing, name='course_listing'),


    #path('hello/', MyView.as_view(), name='my-view'),

]
