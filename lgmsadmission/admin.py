from django.contrib import admin
from django.db.models import F


# Register your models here.

from .models import ContactUs, Inquiry, CasaInquiry, GradeSchoolInquiry, HomeStudyInquiry, HighSchoolInquiry, SpedInquiry


class ContactUsAdmin(admin.ModelAdmin):
    list_display  = ['id', 'firstname','lastname', 'inquryname', 'phonenumber', 'email']
    ordering = ['id', 'inquryname', 'email']


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'phonenumber', 'email', 'programme']
    ordering = ['id','email', 'programme']




class CasaInquiryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'phonenumber', 'inquiryname', 'email', 'programme']
    ordering = ['id','email', 'programme']


class GradeSchoolInquiryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'phonenumber', 'inquiryname', 'email', 'programme']
    ordering = ['id','email', 'programme']



class HighSchoolInquiryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'phonenumber', 'inquiryname', 'email', 'programme']
    ordering = ['id','email', 'programme']


class HomeStudyInquiryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'phonenumber', 'inquiryname', 'email', 'programme']
    ordering = ['id','email', 'programme']
    


class SpedInquiryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'phonenumber', 'inquiryname', 'email', 'programme']
    ordering = ['id','email', 'programme']



admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(CasaInquiry, CasaInquiryAdmin)
admin.site.register(GradeSchoolInquiry, GradeSchoolInquiryAdmin)
admin.site.register(HighSchoolInquiry, HighSchoolInquiryAdmin)
admin.site.register(HomeStudyInquiry, HomeStudyInquiryAdmin)
admin.site.register(SpedInquiry, SpedInquiryAdmin)



