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
    products = Product.objects.all().order_by('name')
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products, "page_number": page_number})

"""
Retrieves all products in the category Books and formats the results
to only display nine product cards per page 
"""
def get_books(request):
    products = Product.objects.filter(category="Books").order_by('price')
    filter = "First Aid Books"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})
    
"""
Retrieves all products in the category Posters and formats the results
to only display nine product cards per page 
"""
def get_posters(request):
    products = Product.objects.filter(category="Posters").order_by('price')
    filter = "First Aid Posters"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})
    
"""
Retrieves all products in the category Extras and formats the results
to only display nine product cards per page 
"""
def get_extras(request):
    products = Product.objects.filter(category="Extras").order_by('price')
    filter = "Extras"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})
    
def get_courses(request):
    products = Product.objects.filter(category="Courses").order_by('price')
    filter = "First Aid Courses"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})

def get_ebooks(request):
    products = Product.objects.filter(category="E-Books").order_by('price')
    filter = "E-Books"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})
    
def get_firstaidkits(request):
    products = Product.objects.filter(category="First Aid Kits").order_by('price')
    filter = "First Aid Kits"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})
    
def get_cds(request):
    products = Product.objects.filter(category="CDs & DVDs").order_by('price')
    filter = "CDs & DVDs"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})
    
def get_manikins(request):
    products = Product.objects.filter(category="Manikins").order_by('price')
    filter = "First Aid Manikins"
    page = request.GET.get('page', 1)
    page_number = page
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "filteredproducts.html", {"products": products, "filter": filter, "page_number": page_number})
    


"""
This view displays the full details of a product to the user
"""
def view_product(request, id):
    products = get_object_or_404(Product, pk=id)
    return render(request, "viewproduct.html", {"products": products})
  
  