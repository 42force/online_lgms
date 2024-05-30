from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import AdminSite

from django.contrib.auth.models import User, Group
from ajax_select import make_ajax_form

from django.conf import settings

from reversion.admin import VersionAdmin
from lgmssis.helper_functions import ReadPermissionModelAdmin
from custom_field.custom_field import CustomFieldAdmin
from lgmsschedule.models import CourseEnrollment

from lgmssis.forms import StudentForm

from lgmssis.models import GradeLevel, Faculty, CountryOption, Applicant, Enquire, StudentHealthRecord, Student, Cohort, TranscriptNote, ClassYear

from lgmsschedule.models import CourseEnrollment, AwardStudent

from ajax_select.fields import autoselect_fields_check_can_add


import sys

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



class StudentHealthRecordInline(admin.TabularInline):
    model = StudentHealthRecord
    extra = 0


class StudentAwardInline(admin.TabularInline):
    model = AwardStudent
    extra = 0

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

class TranscriptNoteInline(admin.TabularInline):
    model = TranscriptNote
    extra = 0



###test only originally from lgmssis..
# class StudentCourse(Student):
#     class Meta:
#         proxy = True


class StudentAdmin(admin.ModelAdmin):
    list_display = ['lrn_no', 'user_students']



class StudentCourseInline(admin.TabularInline):
    model = CourseEnrollment
    form = make_ajax_form(CourseEnrollment, {'course':'course','exclude_days':'day'})
    raw_id_fields = ('course',)
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['course'],
    }
    fields = ['course', 'attendance_note', 'exclude_days']
    extra = 0


class StudentAdmin(VersionAdmin, ReadPermissionModelAdmin, CustomFieldAdmin):
    def changelist_view(self, request, extra_context=None):
        """override to hide inactive students by default"""
        try:
            test = request.META['HTTP_REFERER'].split(request.META['PATH_INFO'])
            if test and test[-1] and not test[-1].startswith('?') and not request.GET.has_key('inactive__exact') and not request.GET.has_key('id__in'):
                return HttpResponseRedirect("/admin/lgmssis/student/?inactive__exact=0")
                #admin/lgmssis/student/change_list.html
        except: pass # In case there is no referer
        return super(StudentAdmin,self).changelist_view(request, extra_context=extra_context)


    def lookup_allowed(self, lookup, *args, **kwargs):
        if lookup in ('id', 'id__in', 'year__id__exact'):
            return True
        return super(StudentAdmin, self).lookup_allowed(lookup, *args, **kwargs)

    def render_change_form(self, request, context, *args, **kwargs):
        try:
            if context['original'].pic:
                txt = '<img src="' + str(context['original'].pic.url_70x65) + '"/>'
                context['adminform'].form.fields['pic'].help_text += txt
        except:
            print("Error in StudentAdmin render_change_form", file=sys.stderr)
    

        if 'lgmsbenchmarkgrade' in settings.INSTALLED_APPS:
            context['adminform'].form.fields['family_access_users'].queryset = User.objects.filter(groups__name='family')

        return super(StudentAdmin, self).render_change_form(request, context,  *args, **kwargs)

    def change_view(self, request, object_id, extra_context=None):
        courses = Course.objects.filter(courseenrollment__user__id=object_id, marking_period__school_year__active_year=True).distinct()
        for course in courses:
            course.enroll = course.courseenrollment_set.get(user__id=object_id).id
        other_courses = Course.objects.filter(courseenrollment__user__id=object_id, marking_period__school_year__active_year=False).distinct()
        for course in other_courses:
            course.enroll = course.courseenrollment_set.get(user__id=object_id).id
        my_context = {
            'courses': courses,
            'other_courses': other_courses,
        }
        return super(StudentAdmin, self).change_view(request, object_id, extra_context=my_context)

    def save_model(self, request, obj, form, change):
        super(StudentAdmin, self).save_model(request, obj, form, change)
        form.save_m2m()
        if 'lgmsbenchmarkgrade' in settings.INSTALLED_APPS:
            group = Group.objects.get_or_create(name='family')[0]
            for user in obj.family_access_users.all():
                user.groups.add(group)
                user.save()


    def get_form(self, request, obj=None, **kwargs):
        exclude = []
        if not request.user.has_perm('sis.view_ssn_student'):
            exclude.append('ssn')
        if not 'lgmsbenchmarkgrade' in settings.INSTALLED_APPS:
            exclude.append('family_access_users')
        if len(exclude):
            kwargs['exclude'] = exclude
        form = super(StudentAdmin,self).get_form(request,obj,**kwargs)
        autoselect_fields_check_can_add(StudentForm, self.model ,request.user)
        return form

    fieldsets = [
        (None, {'fields': [('last_name', 'first_name'), ('year'), ('date_dismissed','reason_left'), 'username', 'grad_date', 'pic', ('sex', 'bday'), 'class_of_year',('unique_id','lrn_no'),
             'parent_email', 'notes', 'siblings',]}),
    ]
    if 'lgmsbenchmarkgrade' in settings.INSTALLED_APPS:
        fieldsets[0][1]['fields'].append('family_access_users')
    change_list_template = "admin/lgmssis/student/change_list.html"
    form = StudentForm
    search_fields = ['first_name', 'last_name', 'username', 'lrn_no', 'streetname', 'state', 'zip', 'id']
    inlines = [StudentHealthRecordInline, TranscriptNoteInline, StudentAwardInline]
    actions = [promote_to_worker, mark_inactive]
    #list_filter = ['inactive','year']
    #list_display = ['__str__','year']
    if 'lgmsbenchmarkgrade' in settings.INSTALLED_APPS:
        #filter_horizontal = ('family_access_users',)

        try:
            from admin_import.options import add_import
        except ImportError:
            pass
        else:
            add_import(StudentAdmin, add_button=True)

admin.site.register(Student, StudentAdmin)
admin.site.register(ClassYear)

class StudentCourse(Student):
    class Meta:
        proxy = True



class StudentCourseAdmin(admin.ModelAdmin):
    inlines = [StudentCourseInline]
    search_fields = [ 'first_name', 'last_name', 'username','lrn_no', 'streetname', 'zip', 'unique_id']
    fields = ['first_name', 'zip', 'username', 'unique_id']
    #list_filter = ['inactive','year']
    #readonly_fields = fields
admin.site.register(StudentCourse, StudentCourseAdmin)




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
#admin.site.register(Student, StudentAdmin)







class SchoolYearAdmin(admin.ModelAdmin):
    pass 




admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(CountryOption, CountryOptionAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(GradeLevel)
# admin.site.register(Applicant, ApplicantAdmin)
# admin.site.register(Enquire, EnquireAdmin)