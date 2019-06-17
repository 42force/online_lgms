from django import forms

from .models import ContactUs, Inquiry







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


