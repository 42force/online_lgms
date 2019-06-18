from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import AdminSite

from django.conf import settings

#from reversion.admin import VersionAdmin
#from lgmssis.helper_functions import ReadPermissionModelAdmin, CustomFieldAdmin

from .models import Faculty, CountryOption, Applicant, Enquire, StudentHealthRecord, Student, Cohort

from lgmsschedule.models import CourseEnrollment
#from lgmsschedule.models import CourseEnrollment

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


class FacultyAdmin(admin.ModelAdmin):
    fields = ['fuser', 'altemail', 'number', 'ext', 'teacher']



class CountryOptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



# class ApplicantAdmin(admin.ModelAdmin):
#     list_display = ['id', 'fname', 'lname']


# class EnquireAdmin(admin.ModelAdmin):
#     list_display = ['id', 'fullname', 'email', 'mobilenumber', 'place', 'programme']


def promote_to_worker(modeladmin, request, queryset):
    for object in queryset:
        object.promote_to_worker()
        LogEntry.objects.log_action(
                    user_id         = request.user.pk,
                    content_type_id = ContentType.objects.get_for_model(object).pk,
                    object_id       = object.pk,
                    object_repr     = unicode(object),
                    action_flag     = CHANGE
                )

def mark_inactive(modeladmin, request, queryset):
    for object in queryset:
        object.inactive=True
        LogEntry.objects.log_action(
                    user_id         = request.user.pk,
                    content_type_id = ContentType.objects.get_for_model(object).pk,
                    object_id       = object.pk,
                    object_repr     = unicode(object),
                    action_flag     = CHANGE
                )
        object.save()


class StudentHealthRecordInline(admin.TabularInline):
    model = StudentHealthRecord
    extra = 0

### Second student admin just for courses
class SubjectCourse(Student):
    class Meta:
        proxy = True


class SubjectCourseAdmin(admin.ModelAdmin):
    #inlines = [SubjectCourseInline]
    search_fields = ['fname', 'lname', 'username', 'unique_id', 'street', 'state', 'zip']
    fields = ['fname', 'lname']
    #list_filter = ['inactive','year']
    #readonly_fields = fields
admin.site.register(SubjectCourse, SubjectCourseAdmin)



class CohortAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)

    def queryset(self, request):
        # exclude PerCourseCohorts from Cohort admin
        qs = super(CohortAdmin, self).queryset(request)
        return qs.filter(percoursecohort=None)

    def save_model(self, request, obj, form, change):
        if obj.id:
            prev_students = Cohort.objects.get(id=obj.id).students.all()
        else:
            prev_students = Student.objects.none()

        # Django is retarded about querysets,
        # save these ids because the queryset will just change later
        student_ids = []
        for student in prev_students:
            student_ids.append(student.id)

        super(CohortAdmin, self).save_model(request, obj, form, change)
        form.save_m2m()

        for student in obj.students.all() | Student.objects.filter(id__in=student_ids):
            student.cache_cohorts()
            student.save()

admin.site.register(Cohort, CohortAdmin)

# class PerCourseCohortAdmin(CohortAdmin):
#     exclude = ('primary',)

#     def __get_teacher_courses(self, username):
#         from django.db.models import Q
#         from ecwsp.schedule.models import Course
#         try:
#             teacher = Faculty.objects.get(username=username)
#             teacher_courses = Course.objects.filter(Q(teacher=teacher) | Q(secondary_teachers=teacher)).distinct()
#         except:
#             teacher_courses = []
#             import traceback
#             print (traceback.format_exc())
#         return teacher_courses

#     def queryset(self, request):
#         qs = super(CohortAdmin, self).queryset(request)
#         if request.user.is_superuser or request.user.groups.filter(name='registrar').count():
#             return qs
#         return qs.filter(course__in=self.__get_teacher_courses(request.user.username))

#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         # TODO: use a wizard or something and filter by THIS COHORT'S COURSE instead of all the teacher's courses
#         if db_field.name == 'students':
#             if not request.user.is_superuser and not request.user.groups.filter(name='registrar').count():
#                 kwargs['queryset'] = Student.objects.filter(course__in=self.__get_teacher_courses(request.user.username))
#         return super(PerCourseCohortAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


# admin.site.register(PerCourseCohort, PerCourseCohortAdmin)

# admin.site.register(ReasonLeft)
# admin.site.register(ReportField)

# admin.site.register(TranscriptNoteChoices)

class SchoolYearAdmin(admin.ModelAdmin):

    pass 
#     def get_form(self, request, obj=None, **kwargs):
#         form = super(SchoolYearAdmin, self).get_form(request, obj, **kwargs)
#         if not 'lgmsbenchmarkgrade' in settings.INSTALLED_APPS:
#             self.exclude = ('benchmark_grade',)
#         return form
#     inlines = [MarkingPeriodInline]
# admin.site.register(SchoolYear, SchoolYearAdmin)

# class ImportLogAdmin(admin.ModelAdmin):
#     list_display = ['user','date','errors']
#     search_fields = ['user__username', 'user__first_name', 'user__last_name']
# admin.site.register(ImportLog, ImportLogAdmin)

# admin.site.register(MessageToStudent)

from django.contrib.auth.admin import UserAdmin
class FamilyAccessUserAdmin(UserAdmin,admin.ModelAdmin):
    fields = ('is_active','username','first_name','last_name','password')
    fieldsets = None
    list_display = ('username','first_name','last_name','is_active',)
#    list_filter = ('is_active','workteam')
    def queryset(self,request):
        return User.objects.filter(groups__name='family')
if 'ecwsp.benchmark_grade' in settings.INSTALLED_APPS:
    admin.site.register(FamilyAccessUser,FamilyAccessUserAdmin)


#this is from the sis - original admin page
######will try to import#########


class StudentCourseInline(admin.TabularInline):
    model = CourseEnrollment
    #form = make_ajax_form(CourseEnrollment, {'course':'course','exclude_days':'day'})
    raw_id_fields = ('course',)
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['course'],
    }
    fields = ['course', 'attendance_note', 'exclude_days']
    extra = 0


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(CountryOption, CountryOptionAdmin)
admin.site.register(Faculty, FacultyAdmin)
# admin.site.register(Applicant, ApplicantAdmin)
# admin.site.register(Enquire, EnquireAdmin)