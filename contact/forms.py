from django import forms


class ContactForm(forms.Form):
	""" Form for contact page """
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.CharField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)

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
		}

		self.fields['message'].widget.attrs = {'rows': 8}
		self.fields['first_name'].widget.attrs['autofocus'] = True
		for field in self.fields:
			placeholder = f'{placeholders[field]} *'
			self.fields[field].widget.attrs['placeholder'] = placeholder
			self.fields[field].label = False