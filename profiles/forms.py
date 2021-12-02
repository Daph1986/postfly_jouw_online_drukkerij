from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Order form which is displayed at checkout page """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_company_name': 'Company name',
            'default_phone_number': 'Phone number',
            'default_postcode': 'Postal code',
            'default_town_or_city': 'Town or city',
            'default_street_address1': 'Street address + house number',
            'default_street_address2': 'Additional address information',
        }

        self.fields['default_company_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form'
            self.fields[field].label = False
