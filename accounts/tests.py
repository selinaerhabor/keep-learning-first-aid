from django.test import TestCase
from accounts.forms import UserAccountForm, UserRegistrationForm

# Testing Registration Form works as intended
class TestRegistrationForm(TestCase):
    
    def registration_form_denied_for_password_mismatch(self):
        register_form = UserRegistrationForm({
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john.smith@test.com',
            'password1': 'test123',
            'password2': 'test987',
        })
        self.assertFalse(register_form.is_valid())
        
        
    def registration_form_requires_five_values(self):
        register_form = UserRegistrationForm({
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john.smith@test.com',
            'password1': 'test123',
            'password2': 'test123',
        })
        self.assertTrue(register_form.is_valid())
        
        
# Testing Login Form works as intended
class TestLoginForm(TestCase):
    
    def login_form_requires_password(self):
        login_form = UserAccountForm({
            'email': 'john.smith@test.com',
        })
        self.assertFalse(login_form.is_valid())
        
        
    def login_form_test(self):
        login_form = UserAccountForm({
            'username': 'john.smith@test.com',
            'password': 'test123',
        })
        self.assertTrue(login_form.is_valid())


    def login_only_for_registered_users(self):
        login_user = self.client.login(username='john.s@test.com', password='test123')
        self.assertFalse(login_user)
