from django.shortcuts import render, redirect

# Create your views here.

from .forms import ContactUsForm, InquiryForm, CasaInquiryForm, GradeSchoolInquiryForm, HighSchoolInquiryForm, SpedInquiryForm, HomeStudyInquiryForm, CasaApplicationForm, DocumentForm 
from django.core.mail import EmailMessage

from django.core.mail import send_mail
from django.conf import settings

def thankyou_inquiry(request):
    return render(request, 'lgmsadmission/thankyouinquiry.html')


def thankyou_upload(request):
    return render(request, 'lgmsadmission/thankyouupload.html')

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
            return redirect('thankyou_inquiry')
    else:
        casainquiry_form = CasaInquiryForm()
    return render(request, 'lgmsadmission/casainquiry.html', {'casainquiry_form' : casainquiry_form})



def gradeschool_inquiry(request):
    if request.method == 'POST':
        gsinquiry_form = GradeSchoolInquiryForm(request.POST)
        if gsinquiry_form.is_valid():
            gsinquiry_form.save()
            mail_subject = 'Thank you for your Inquiry in '
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = gsinquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('thankyou_inquiry')
    else:
        gsinquiry_form = GradeSchoolInquiryForm()
    return render(request, 'lgmsadmission/gradeschoolinquiry.html', {'gsinquiry_form' : gsinquiry_form})



def hs_inquiry(request):
    if request.method == 'POST':
        hsinquiry_form = HighSchoolInquiryForm(request.POST)
        if hsinquiry_form.is_valid():
            hsinquiry_form.save()
            mail_subject = 'Thank you for your Inquiry in our High School Programme'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = hsinquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('thankyou_inquiry')
    else:
        hsinquiry_form = HighSchoolInquiryForm()
    return render(request, 'lgmsadmission/hsinquiry.html', {'hsinquiry_form' : hsinquiry_form})



def homestudy_inquiry(request):
    if request.method == 'POST':
        homestudyinquiry_form = HomeStudyInquiryForm(request.POST)
        if homestudyinquiry_form.is_valid():
            homestudyinquiry_form.save()
            mail_subject = 'Thank you for your Inquiry in our High School Programme'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = homestudyinquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('thankyou_inquiry')
    else:
        homestudyinquiry_form = HomeStudyInquiryForm()
    return render(request, 'lgmsadmission/homestudyinquiry.html', {'homestudyinquiry_form' : homestudyinquiry_form})



def sped_inquiry(request):
    if request.method == 'POST':
        spedinquiry_form = SpedInquiryForm(request.POST)
        if spedinquiry_form.is_valid():
            spedinquiry_form.save()
            mail_subject = 'Thank you for your Inquiry in our High School Programme'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = spedinquiry_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('thankyou_inquiry')
    else:
        spedinquiry_form = SpedInquiryForm()
    return render(request, 'lgmsadmission/spedinquiry.html', {'spedinquiry_form' : spedinquiry_form})



def casa_applyform(request):
    if request.method == 'POST':
        caapply_form = CasaApplicationForm(request.POST)
        doc_form = DocumentForm(request.POST, request.FILES)
        if caapply_form.is_valid() and doc_form.is_valid():
            caapply_form.save()
            doc_form.save()
            mail_subject = 'Thank you for your Inquiry in our High School Programme'
            message = 'Inquiry Received, we will be in touch shortly'
            to_email = caapply_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('thankyou_inquiry')
    else:
        caapply_form = CasaApplicationForm()
        doc_form = DocumentForm()

        context = {
            'caapply_form' : caapply_form,
            'doc_form' : doc_form
        }
    return render(request, 'lgmsadmission/casaapplication.html', context)


def model_form_upload(request):
    if request.method == 'POST':
        doc_form = DocumentForm(request.POST, request.FILES)
        if doc_form.is_valid():
            doc_form.save()
            return redirect('thankyou_upload')
    else:
        doc_form = DocumentForm()
    return render(request, 'lgmsadmission/casaapplication.html', {
        'doc_form': doc_form
    })

