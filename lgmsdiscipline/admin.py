from django.contrib import admin


from ajax_select import make_ajax_form
#from daterange_filter.filter import DateRangeFilter

from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from . models import DisciplineAction, DisciplineActionInstance, StudentDiscipline, Infraction

# Register your models here.


class DisciplineActionInstanceInline(admin.TabularInline):
    model = DisciplineActionInstance
    extra = 1

class StudentDisciplineAdmin(admin.ModelAdmin):
    form = make_ajax_form(StudentDiscipline, dict(students='discstudent'))

    list_per_page = 50
    fields = ['date', 'students', 'teacher', 'infraction', 'comments', 'private_note']
    list_display = ('show_students', 'date', 'comment_Brief', 'infraction')
    list_filter = [('date',DateRangeFilter), 'infraction', 'action',]
    search_fields = ['comments', 'students__fname', 'students__lname']
    inlines = [DisciplineActionInstanceInline]

    def lookup_allowed(self, lookup, *args, **kwargs):
        if lookup in ('students','students__id__exact',):
            return True
        return super(StudentDisciplineAdmin, self).lookup_allowed(lookup, *args, **kwargs)

admin.site.register(StudentDiscipline, StudentDisciplineAdmin)
admin.site.register(DisciplineAction)
admin.site.register(Infraction)
