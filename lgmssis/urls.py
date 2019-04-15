from django.urls import path
#from lgmssis.views import MyView

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('courselist/', views.courselist, name='course'),


    #path('hello/', MyView.as_view(), name='my-view'),

]
