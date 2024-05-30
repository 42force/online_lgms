from django.contrib import admin
from django.db.models import F


from rangefilter.filter import DateRangeFilter

# Register your models here.

from .models import ApplicantStandardCategoryGrade, ApplicantStandardTestResult, ContactUs, Inquiry, CasaInquiry, GradeSchoolInquiry, HomeStudyInquiry, HighSchoolInquiry, SpedInquiry, CasaApplication


class ContactUsAdmin(admin.ModelAdmin):
    list_display  = ['id', 'firstname','lastname', 'inquryname', 'phonenumber', 'email']
    ordering = ['id', 'inquryname', 'email']


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'phonenumber', 'email', 'programme', 'date']
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




class ApplicantStandardCategoryGradeInline(admin.TabularInline):
    model = ApplicantStandardCategoryGrade
    extra = 1

class ApplicantStandardTestResultAdmin(admin.ModelAdmin):
    inlines = (ApplicantStandardCategoryGradeInline,)
    list_display = ['applicant', 'test', 'date']
    list_filter = ['test', ('date', DateRangeFilter)]
    search_fields = ['applicant__fname', 'applicant__lname', 'test__name']
admin.site.register(ApplicantStandardTestResult, ApplicantStandardTestResultAdmin)




class CasaApplicationAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname',]


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(CasaInquiry, CasaInquiryAdmin)
admin.site.register(GradeSchoolInquiry, GradeSchoolInquiryAdmin)
admin.site.register(HighSchoolInquiry, HighSchoolInquiryAdmin)
admin.site.register(HomeStudyInquiry, HomeStudyInquiryAdmin)
admin.site.register(SpedInquiry, SpedInquiryAdmin)
admin.site.register(CasaApplication, CasaApplicationAdmin )



