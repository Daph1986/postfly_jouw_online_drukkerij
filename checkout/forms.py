from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'company_name', 
				  'email', 'phone_number','street_address1', 
				  'street_address2', 'town_or_city', 'postcode', 
				  'country',)

    def __init__(self, *args, **kwargs):
        """ Order form which is displayed at checkout page """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
			'last_name': 'Last name',
			'company_name': 'Company name',
            'email': 'Email address',
            'phone_number': 'Phone number',
            'postcode': 'Postal code',
            'town_or_city': 'Town or city',
            'street_address1': 'Street address + house number',
            'street_address2': 'Additional address information',
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