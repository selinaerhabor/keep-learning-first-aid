# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def learningforkids(request):
    return render(request, 'learningforkids.html')
    
def quiz(request):
    return render(request, 'learningforkidsquiz.html')