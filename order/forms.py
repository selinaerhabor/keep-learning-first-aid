from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=True)
    cvv = forms.CharField(label='Security code (CVV)', required=True)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'title', 'first_name', 'last_name', 'phone_number', 'country', 'address_line_1', 'address_line_2', 'town_or_city', 'county', 'postcode'
        )