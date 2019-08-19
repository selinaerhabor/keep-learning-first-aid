from django.test import TestCase
from .models import Firstaidtip

class Firstaidtiptests(TestCase):

    def test_str(self):
        test_title = Firstaidtip(name='title')
        self.assertEqual(str(test_title), 'title')
