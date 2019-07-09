# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def learningforadults(request):
    return render(request, 'learningforadults.html')