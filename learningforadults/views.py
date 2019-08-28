# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from products.models import Product


# Displays Featured products on Learning For Adults Page (4)
def learningforadults(request):
    products = Product.objects.filter(featured="Y")
    return render(request, 'learningforadults.html', {"products": products})

# Displays Featured product full details     

"""
Redirects users to an interactive quiz aimed at adults via 'Begin Test' 
button, which has 15 multiple choice questions and gives players feedback after
completion of quiz
"""
def learningforadultsquiz(request):
    return render(request, "learningforadultsquiz.html")
    
    