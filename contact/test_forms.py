from django.test import TestCase
from contact.forms import ContactForm


class TestContactForm(TestCase):
    """
    Tests the contactform if the required fields
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
                         [0], 'This field is required.')
        self.assertEqual(form.errors['last_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['email']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['subject']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['message']
                         [0], 'This field is required.')
