from django.shortcuts import render

# Create your views here.

from .forms import ContactUsForm


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            mail_subject = 'Thank you for your Inquiry'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = contact_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    else:
        contact_form = ContactUsForm()
    return render(request, 'lgmsadmission/contactform.html', {'contact_form' : contact_form})
