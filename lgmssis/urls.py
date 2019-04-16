from django.urls import path
#from lgmssis.views import MyView
from . import views

app_name= 'lgmssis'

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login')


    #path('hello/', MyView.as_view(), name='my-view'),

]
