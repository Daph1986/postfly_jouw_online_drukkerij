from django.test import TestCase
from contact.forms import ContactForm, SampleKitForm, QuotationForm


class TestContactForm(TestCase):
    """
    Tests the contact form if the required fields
    are indeed required.
    """

    def test_required_fields(self):
        form = ContactForm({
            'first_name': '',
            'last_name': '',
            'email': '',
            'subject': '',
            'message': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('subject', form.errors.keys())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['first_name']
                         [0], 'This field is required.', 'Dit veld is verplicht.')
        self.assertEqual(form.errors['last_name']
                         [0], 'This field is required.', 'Dit veld is verplicht.')
        self.assertEqual(form.errors['email']
                         [0], 'This field is required.', 'Dit veld is verplicht.')
        self.assertEqual(form.errors['subject']
                         [0], 'This field is required.', 'Dit veld is verplicht.')
        self.assertEqual(form.errors['message']
                         [0], 'This field is required.', 'Dit veld is verplicht.')


class TestSampleKitForm(TestCase):
    """
    Tests the sample kit form if the required fields
    are indeed required.
    """

    def test_required_fields(self):
        form = SampleKitForm({
            'first_name': '',
            'last_name': '',
            'email': '',
            'street_address1': '',
            'postcode': '',
            'town_or_city': '',
            'country': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('street_address1', form.errors.keys())
        self.assertIn('postcode', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['first_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['last_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['email']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['street_address1']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['postcode']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['town_or_city']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['country']
                         [0], 'This field is required.')


class TestQuotationForm(TestCase):
    """
    Tests the quotation form if the required fields
    are indeed required.
    """

    def test_required_fields(self):
        form = QuotationForm({
            'first_name': '',
            'last_name': '',
            'email': '',
            'street_address1': '',
            'postcode': '',
            'town_or_city': '',
            'country': '',
            'message': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('street_address1', form.errors.keys())
        self.assertIn('postcode', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('country', form.errors.keys())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['first_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['last_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['email']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['street_address1']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['postcode']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['town_or_city']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['country']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['message']
                         [0], 'This field is required.')

