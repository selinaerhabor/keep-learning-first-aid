from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

# Testing Make Payment Form works properly
class MakePaymentFormTest(TestCase):
    def test_submit_with_required_input(self):
        payment_form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': "567",
                    'expiry_month': 1,
                    'expiry_year': 2020,
                    'stripe_id': 'l'
        })
        self.assertTrue(payment_form.is_valid())
        
    
    def test_submit_without_required_input(self):
        payment_form = MakePaymentForm({
                    'credit_card_number': '', 
                    'cvv': '567', 
                    'expiry_month': 1,
                    'expiry_year': 2020,
        })
        self.assertFalse(payment_form.is_valid())


# Testing Order Form works properly
class OrderFormTest(TestCase):
    def test_submit_required_input(self):
        order_form = OrderForm({
                    'title': 'Mr',
                    'first_name': 'John',
                    'last_name': 'Smith',
                    'phone_number': '01234567890',
                    'country': 'United Kingdom',
                    'address_line_1': '1 Test Road',
                    'address_line_2': '',
                    'town_or_city': 'London',
                    'county': '',
                    'postcode': 'TE15 2ST',
        })
        self.assertTrue(order_form.is_valid())
        
    
    
    def test_submit_missing_required_input(self):
        order_form = OrderForm({
                    'title': 'Mr',
                    'first_name': 'John',
                    'last_name': '',
                    'phone_number': '01234567890',
                    'country': 'United Kingdom',
                    'address_line_1': '1 Test Road',
                    'address_line_2': '',
                    'town_or_city': 'London',
                    'county': '',
                    'postcode': 'TE15 2ST',
        })
        self.assertFalse(order_form.is_valid())