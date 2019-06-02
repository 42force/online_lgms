from django.contrib import admin

from .models import Profile, Application

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'image', 'bio','streetname', 'cityname', 'mobilenumber',]


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'streetname']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Application, ApplicationAdmin)

