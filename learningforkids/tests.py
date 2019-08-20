# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Kidsquestion
import random

class Kidsquestiontests(TestCase):

    def test_str(self):
        test_question = Kidsquestion(name='question')
        self.assertEqual(str(test_question), 'question')
        
class QuizTests(TestCase):
    
    # Tests to shuffle quiz questions
    
    def question(self):
        order = ['a','b','c','d']
        random.shuffle(order)
        order
        self.assertNotEqual(str(order), ['a','b','c','d'])
