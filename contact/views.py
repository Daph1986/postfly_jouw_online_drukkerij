from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string

from profiles.models import UserProfile

from .forms import ContactForm

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
            return redirect('/contact',
                            messages.success(request, f'Thank you for contacting \
                                            us. We will be in touch sortly.'))
    
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def sample_kit(request):
    """View to return our sample request page"""

    return render(request, 'contact/sample.html')


def quotation(request):
    """View to return our quotation page"""

    return render(request, 'contact/quotation.html')