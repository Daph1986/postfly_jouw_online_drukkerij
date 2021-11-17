from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string

from profiles.models import UserProfile

from .forms import ContactForm, SampleKitForm, QuotationForm

def contact(request):
    """View to return our contact page with the contact form"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'email': profile.user.email,
                    }
                )
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            first_name = contact_form.cleaned_data['first_name']
            last_name = contact_form.cleaned_data['last_name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            html_msg = render_to_string(
                'emails/contact_email.html',
                {'first_name': first_name, 'last_name': last_name, 'subject': subject, 'message': message})
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [
                    email, settings.EMAIL_HOST_USER],
                    html_message=html_msg, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('home'),
                            messages.success(request, f'Thank you for \
                                            contacting us. A copy of your \
                                            message has been send to your \
                                            email. We will be in touch \
                                            sortly.'))
    
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def sample_kit(request):
    """View to return the request sample kit page with the form"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                sample_kit_form = SampleKitForm(initial={
                    'email': profile.user.email,
                    'company_name': profile.default_company_name,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'country': profile.default_country,
                    'phone_number': profile.default_phone_number,
                    }
                )
            except UserProfile.DoesNotExist:
                sample_kit_form = SampleKitForm()
        else:
            sample_kit_form = SampleKitForm()
    else:
        sample_kit_form = SampleKitForm(request.POST)
        if sample_kit_form.is_valid():
            first_name = sample_kit_form.cleaned_data['first_name']
            last_name = sample_kit_form.cleaned_data['last_name']
            email = sample_kit_form.cleaned_data['email']
            company_name = sample_kit_form.cleaned_data['company_name']
            street_address1 = sample_kit_form.cleaned_data['street_address1']
            street_address2 = sample_kit_form.cleaned_data['street_address2']
            postcode = sample_kit_form.cleaned_data['postcode']
            town_or_city = sample_kit_form.cleaned_data['town_or_city']
            country = sample_kit_form.cleaned_data['country']
            phone_number = sample_kit_form.cleaned_data['phone_number']
            html_msg = render_to_string(
                'emails/sample_kit_email.html',
                {'first_name': first_name, \
                 'last_name': last_name, \
                 'company_name': company_name, \
                 'street_address1': street_address1, \
                 'street_address2': street_address2, \
                 'postcode': postcode, \
                 'town_or_city': town_or_city, \
                 'country': country, \
                 'phone_number': phone_number})
            try:
                send_mail(first_name, last_name, settings.EMAIL_HOST_USER, [
                    email, settings.EMAIL_HOST_USER],
                    html_message=html_msg, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('home'),
                            messages.success(request, f'Thank you for your \
                                            request. A copy of your request \
                                            has been send to your email. \
                                            Your free sample kit will be \
                                            shipped as soon as possible.'))
    
    template = 'contact/sample.html'
    context = {
        'sample_kit_form': sample_kit_form,
    }

    return render(request, template, context)

def quotation(request):
    """View to return our quotation page with the form"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                quotation_form = QuotationForm(initial={
                    'email': profile.user.email,
                    'company_name': profile.default_company_name,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'country': profile.default_country,
                    'phone_number': profile.default_phone_number,
                    }
                )
            except UserProfile.DoesNotExist:
                quotation_form = QuotationForm()
        else:
            quotation_form = QuotationForm()
    else:
        quotation_form = QuotationForm(request.POST)
        if quotation_form.is_valid():
            first_name = quotation_form.cleaned_data['first_name']
            last_name = quotation_form.cleaned_data['last_name']
            email = quotation_form.cleaned_data['email']
            company_name = quotation_form.cleaned_data['company_name']
            street_address1 = quotation_form.cleaned_data['street_address1']
            street_address2 = quotation_form.cleaned_data['street_address2']
            postcode = quotation_form.cleaned_data['postcode']
            town_or_city = quotation_form.cleaned_data['town_or_city']
            country = quotation_form.cleaned_data['country']
            phone_number = quotation_form.cleaned_data['phone_number']
            message = quotation_form.cleaned_data['message']
            html_msg = render_to_string(
                'emails/quotation_email.html',
                {'first_name': first_name, 'last_name': last_name, \
                 'message': message, \
                 'company_name': company_name, \
                 'street_address1': street_address1, \
                 'street_address2': street_address2,'postcode': postcode, \
                 'town_or_city': town_or_city, 'country': country, \
                 'phone_number': phone_number})
            try:
                send_mail(first_name, last_name, settings.EMAIL_HOST_USER, [
                    email, settings.EMAIL_HOST_USER],
                    html_message=html_msg, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('home'),
                            messages.success(request, f'Thank you for your \
                                            request. A copy of your request \
                                            has been send to your email. \
                                            We will send you a quotation \
                                            as soon as possible.'))
    
    template = 'contact/quotation.html'
    context = {
        'quotation_form': quotation_form,
    }

    return render(request, template, context)