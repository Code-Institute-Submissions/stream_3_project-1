from django.test import TestCase
from .forms import UserRegistrationForm
from django import forms
from django.contrib.auth.models import User

# Create your tests here.

class TestForm(TestCase):
    
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'declan',
            'email': 'declan@example.com',
            'password1': 'password',
            'password2': 'password',
        })
 
        self.assertTrue(form.is_valid())
        
    def test_registration_form_with_different_passwords(self):
        form = UserRegistrationForm({
            'username': 'declan',
            'email': 'declan@example.com',
            'password1': 'password',
            'password2': 'password2',
        })
 
        self.assertFalse(form.is_valid())
        
    
        
        
