from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    
    # Tests run against Product model created
    
    def test_str(self):
        test_name = Product(name='CPR Manikin')
        self.assertEqual(str(test_name), 'CPR Manikin')