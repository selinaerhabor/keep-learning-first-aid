# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#Learning For Adults Quiz Model
class Adultsquestion(models.Model):
    question = models.CharField(max_length=250, default='')
    answer_a = models.CharField(max_length=200, default='')
    answer_b = models.CharField(max_length=200, default='')
    answer_c = models.CharField(max_length=200, default='')
    answer_d = models.CharField(max_length=200, default='')
    correct_answer = models.CharField(max_length=1, default='')
    solution = models.TextField()
    
    def __str__(self):
        return self.question
