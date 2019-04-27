"""online_lgms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('lgmssis/', include('lgmssis.urls')),
    path('', RedirectView.as_view(url='/lgmssis/', permanent=True)),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    #path('accounts/login/', auth_views.LoginView.as_view(template_name='lgmssis/login.html')),

    #this is for the flatpages
    path('home/', views.flatpage, {'url': '/home/'}, name='home'),
    path('page/', views.flatpage, {'url': '/page/'}, name='page'),
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('courses/', views.flatpage, {'url': '/courses/'}, name='courses'),
    path('gallery/', views.flatpage, {'url': '/gallery/'}, name='gallery'),
    path('contact/', views.flatpage, {'url': '/contact/'}, name='contact'),
    path('news/', views.flatpage, {'url': '/news/'}, name='news'),
    path('faq1/', views.flatpage, {'url': '/faq1/'}, name='faq1'),
    path('faq2/', views.flatpage, {'url': '/faq2/'}, name='faq2'),
    path('testimonials/', views.flatpage, {'url': '/testimonials/'}, name='testimonials'),
    path('coming-soon/', views.flatpage, {'url': '/coming-soon/'}, name='coming-soon'),
    path('privacy/', views.flatpage, {'url': '/privacy/'}, name='privacy'),
    path('terms/', views.flatpage, {'url': '/terms/'}, name='terms'),
    path('courses/casa/', views.flatpage, {'url': '/courses/casa/'}, name='casa'),
    path('courses/sped/', views.flatpage, {'url': '/courses/sped/'}, name='sped'),
    path('courses/elementary/', views.flatpage, {'url': '/courses/elementary/'}, name='elementary'),
    path('courses/junior/', views.flatpage, {'url': '/courses/junior/'}, name='junior'),
    path('courses/senior/', views.flatpage, {'url': '/courses/senior/'}, name='senior'),
    path('courses/test/', views.flatpage, {'url': '/courses/test/'}, name='test'),



    #accounts management


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
