from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

class MakePaymentFormTest(TestCase):
    
    def submit_with_required_input_test(self):
        payment_form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': "567",
                    'expiry_month': 1,
                    'expiry_year': 2020,
                    'stripe_id': 'l'
        })
        self.assertTrue(payment_form.is_valid())
        
    
    def submit_without_required_input_test(self):
        payment_form = MakePaymentForm({
                    'credit_card_number': '', 
                    'cvv': '567', 
                    'expiry_month': 8,
                    'expiry_year': 2020,
        })
        self.assertFalse(payment_form.is_valid())
