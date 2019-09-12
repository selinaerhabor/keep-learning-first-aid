from django.test import TestCase
from .models import Firstaidtip

class Firstaidtiptests(TestCase):

    def test_str(self):
        test_title = Firstaidtip(name='What to do when someone is choking')
        self.assertEqual(str(test_title), 'What to do when someone is choking')
