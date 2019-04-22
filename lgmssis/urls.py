from django.urls import path
#from lgmssis.views import MyView
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='indexpage'),

    path('accounts/', include('django.contrib.auth.urls')),

    #path('hello/', MyView.as_view(), name='my-view'),

]
