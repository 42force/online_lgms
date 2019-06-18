from django.contrib import admin


from django.forms import CheckboxSelectMultiple

from ajax_select import make_ajax_form

from . models import StudentMeeting, StudentMeetingCategory, FollowUpAction

# Register your models here.


class StudentMeetingAdmin(admin.ModelAdmin):
    list_display = ['category','display_students','date','reported_by']
    fields = ['category','students','date','notes','file','follow_up_action','follow_up_notes','reported_by']
    form = make_ajax_form(StudentMeeting, dict(students='student'))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'reported_by':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(StudentMeetingAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def lookup_allowed(self, lookup, *args, **kwargs):
        if lookup in ('students__id__exact',):
            return True
        return super(StudentMeetingAdmin, self).lookup_allowed(lookup, *args, **kwargs)

admin.site.register(StudentMeeting, StudentMeetingAdmin)
admin.site.register(StudentMeetingCategory)
admin.site.register(FollowUpAction)