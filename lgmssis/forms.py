from django import forms

from .models import Applicant, Enquire

class ApplyForm(forms.Form):
    model = Applicant
    fields = ()


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


class EnquireForm(forms.ModelForm):
    model = Enquire
    fields = ('fullname', 'email', 'mobile', 'place', 'programme')

    




