from django.shortcuts import render, redirect

# Create your views here.

from .forms import ContactUsForm, InquiryForm
from django.core.mail import EmailMessage

from django.core.mail import send_mail
from django.conf import settings

def thankyou_inquiry(request):
    return render(request, 'lgmsadmission/thankyouinquiry.html')


#contact form
def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            mail_subject = 'Thank you for your Message'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = contact_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('thankyou_inquiry')
    else:
        contact_form = ContactUsForm()
    return render(request, 'lgmsadmission/contactform.html', {'contact_form' : contact_form})


#inquiry form
def inquiry_us(request):
    if request.method == 'POST':
        inquiry_form = InquiryForm(request.POST)
        if inquiry_form.is_valid():
            inquiry_form.save()
            mail_subject = 'Thank you for your Inquiry'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = inquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    else:
        inquiry_form = InquiryForm()
    return render(request, 'lgmsadmission/casainquiry.html', {'inquiry_form' : inquiry_form})


def casa_inquiry(request):
    if request.method == 'POST':
        casainquiry_form = CasaInquiryForm(request.POST)
        if casainquiry_form.is_valid():
            casainquiry_form.save()
            mail_subject = 'Thank you for your Inquiry'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = casainquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    else:
        casainquiry_form = CasaInquiryForm()
    return render(request, 'lgmsadmission/casainquiry.html', {'casainquiry_form' : casainquiry_form})



def gradeschool_inquiry(request):
    if request.method == 'POST':
        gsinquiry_form = GradeSchoolInquiryForm(request.POST)
        if gsinquiry_form.is_valid():
            gsinquiry_form.save()
            mail_subject = 'Thank you for your Inquiry'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = gsinquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    else:
        gsinquiry_form = GradeSchoolInquiryForm()
    return render(request, 'lgmsadmission/gradeschoolinquiry.html', {'gsinquiry_form' : gsinquiry_form})



def hs_inquiry(request):
    if request.method == 'POST':
        gsinquiry_form = GradeSchoolInquiryForm(request.POST)
        if gsinquiry_form.is_valid():
            gsinquiry_form.save()
            mail_subject = 'Thank you for your Inquiry'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = gsinquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    else:
        gsinquiry_form = GradeSchoolInquiryForm()
    return render(request, 'lgmsadmission/gradeschoolinquiry.html', {'gsinquiry_form' : gsinquiry_form})
