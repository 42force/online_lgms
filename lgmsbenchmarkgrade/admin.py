from django.contrib import admin
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE


from .models import Category, Item, Demonstration, Mark, Aggregate, AssignmentType, CalculationRule, CalculationRulePerCourseCategory, CalculationRuleCategoryAsCourse, CalculationRuleSubstitution



class CalculationRulePerCourseCategoryInline(admin.TabularInline):
    model = CalculationRulePerCourseCategory
    verbose_name = 'category included in each course average'
    verbose_name_plural = 'categories included in each course average'
    extra = 0 

class CalculationRuleCategoryAsCourseInline(admin.TabularInline):
    model = CalculationRuleCategoryAsCourse
    verbose_name = 'category treated as course in each marking period average'
    verbose_name_plural = 'categories treated as courses in each marking period average'
    extra = 0

class CalculationRuleSubstitutionInline(admin.TabularInline):
    model = CalculationRuleSubstitution
    verbose_name = 'grade substitution'
    verbose_name_plural = 'grade substitutions'
    extra = 0

class CalculationRuleAdmin(admin.ModelAdmin):
    inlines = [CalculationRulePerCourseCategoryInline, CalculationRuleCategoryAsCourseInline, CalculationRuleSubstitutionInline]

admin.site.register(CalculationRule, CalculationRuleAdmin)






admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Demonstration)
admin.site.register(Mark)
admin.site.register(Aggregate)
admin.site.register(AssignmentType)