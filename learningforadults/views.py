# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Adultsquestion

# Create your views here.
def learningforadults(request):
    return render(request, 'learningforadults.html')
    

"""
Redirects users to an interactive quiz aimed at adults, which has 
15 multiple choice questions and gives players feedback after
completion of quiz
"""
def learningforadultsquiz(request):
    adultsquestions = Adultsquestion.objects.all()
    return render(request, "learningforadultsquiz.html", {"adultsquestions": adultsquestions})