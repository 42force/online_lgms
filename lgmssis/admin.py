from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import AdminSite

from .models import CountryOption, Applicant

admin.site.site_header = 'Learning Garden Montessori Administration'

# Register your models here.

class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields' : ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes':('collapse',),
            'fields':(
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),

    )


class CountryOptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname']


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(CountryOption, CountryOptionAdmin)
admin.site.register(Applicant, ApplicantAdmin)