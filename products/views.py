# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product

"""
View to show First Aid Learning Materials and Equipment available for 
purchase on the website
"""
def sale(request):
    
    products = Product.objects.all().order_by('category')
    page = request.GET.get('page', 1)
    
    paginator = Paginator(products, 10)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
        
    return render(request, "products.html", {"products": products})
    

def view_product(request, id):
    """
    This view displays the full details of a product to the user
    """
    products = get_object_or_404(Product, pk=id)
    return render(request, "viewproduct.html", {"products": products})

  