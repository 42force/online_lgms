from django import forms

from .models import ContactUs, Inquiry, Document, CasaApplication


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions




class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['firstname', 'lastname', 'inquryname', 'phonenumber', 'email', 'id' ]



class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['firstname', 'phonenumber', 'email', 'programme', 'id']



class CasaInquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['firstname', 'phonenumber', 'email', 'programme', 'id']


class GradeSchoolInquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['firstname', 'phonenumber', 'email', 'programme', 'id']


class HighSchoolInquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['firstname', 'phonenumber', 'email', 'programme', 'id']



class HomeStudyInquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['firstname', 'phonenumber', 'email', 'programme', 'id']


class SpedInquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['firstname', 'phonenumber', 'email', 'programme', 'id']



class CasaApplicationForm(forms.ModelForm):

    seshoption = {('7:30', '7:30 Class'),
        ('10:30', '10:30 Class'),
        ('1:30', '1:30 Class')}

    sessionchoice = forms.ChoiceField(label="Choose Class Time", widget=forms.RadioSelect, choices=seshoption)
    

    reportcard = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((0, 'No'), (1, 'Yes')),
        widget=forms.RadioSelect(attrs={'class': 'inline'}), label="Submitted Report Card"
    )
    

    class Meta:
        model = CasaApplication
        fields = (
        'fname', 
        'lname', 
        'bday', 
        'pic', 
        'streetname', 
        'cityname', 
        'country_of_birth', 
        'mobilenumber',
        'parent_guardian_first_name',
        'parent_guardian_last_name',
        'parent_guardian_occupation',
        'parent_guardian_company_firm',
        'company_firm_address',
        'company_firm_phone',
        'relationship_to_student',
        'email',
        'howdidyouhear',
        'name_of_children',
        'present_school',
        'present_school_address',
        'years_of_attend',
        )


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            parent_guardian_first_name = self.fields['parent_guardian_first_name']                                    
            parent_guardian_first_name.choices = list(parent_guardian_first_name.choices)
            parent_guardian_first_name.choices.append(tuple(('add_new_parent_guardian', 'Add New Parent or Guardian')))


        helper = FormHelper()
        helper.form_class = 'form-horizontal'



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )