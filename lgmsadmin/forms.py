#from ecwsp.work_study.models import *
from lgmsadmin.models import *

from django import forms
from django.contrib.admin import widgets as adminwidgets
# from django.contrib.localflavor.us.forms import *
# from django.contrib.formtools.wizard.views import WizardView
# from django.contrib.formtools.wizard import FormWizard
from django.utils.safestring import mark_safe
# from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.shortcuts import render
from django.template import RequestContext

from django.conf import settings

from decimal import Decimal
from datetime import datetime, date

# class TemplateForm(forms.ModelForm):
#     class Meta:
#         model = TimeSheet
#         fields = '__all__'

#     def clean(self):
#         super(TemplateForm, self).clean()
#         if self.cleaned_data.get('file'):
#             file = self.cleaned_data['file'].name
#             type = file.split('.')[-1]
#             if not type in ['odt', 'ods', 'xls', 'xlsx']:
#                 raise forms.ValidationError("Must be odt, ods, or xls file.")
#         return self.cleaned_data
