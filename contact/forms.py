from django import forms
from django_countries.fields import CountryField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    """ Form for the contact page """
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(attrs={'required_score':0.75}),
    )

    def __init__(self, *args, **kwargs):
        """ 
        Contact form which is displayed at contact page with placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email address',
            'subject': 'Subject',
            'message': 'Message',
            'captcha': 'Captcha'
        }

        self.fields['message'].widget.attrs = {'rows': 8}
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class SampleKitForm(forms.Form):
    """ Form for the sample kit request page """
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    company_name = forms.CharField(required=False)
    street_address1 = forms.CharField(required=True)
    street_address2 = forms.CharField(required=False)
    postcode = forms.CharField(required=True)
    town_or_city = forms.CharField(required=True)
    country = CountryField(blank_label='Select country *').formfield()
    phone_number = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        """ 
        Sample kit form which is displayed at 
        sample kit request page with placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email address',
            'company_name': 'Company name',
            'street_address1': 'Street address + house number',
            'street_address2': 'Additional address information',
            'postcode': 'Postal code',
            'town_or_city': 'Town or city',
            'phone_number': 'Phone number',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class QuotationForm(forms.Form):
    """ Form for the sample kit request page """
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    company_name = forms.CharField(required=False)
    street_address1 = forms.CharField(required=True)
    street_address2 = forms.CharField(required=False)
    postcode = forms.CharField(required=True)
    town_or_city = forms.CharField(required=True)
    country = CountryField(blank_label='Select country *').formfield()
    phone_number = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        """ 
        Sample kit form which is displayed at 
        sample kit request page with placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email address',
            'company_name': 'Company name',
            'street_address1': 'Street address + house number',
            'street_address2': 'Additional address information',
            'postcode': 'Postal code',
            'town_or_city': 'Town or city',
            'phone_number': 'Phone number',
            'message': 'Describe what you want a quotation for',
        }

        self.fields['message'].widget.attrs = {'rows': 8}
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
