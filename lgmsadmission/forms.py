from django import forms

from .models import ContactUs, Inquiry




class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['firstname', 'lastname', 'inquryname', 'phonenumber', 'email' ]



class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['firstname', 'phonenumber', 'email', 'programme']



