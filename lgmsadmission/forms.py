from .models import ContactUs




class ContactUsForm(forms.ModelForm)

class Meta:
        model = Application
        fields = ['fname', 'lname', 'mobilenumber', 'streetname', 'country_of_birth', 'progoption', 'howdidyouhear' ]
