from django.shortcuts import render
from .models import Product

# Create your views here.
def sale(request):
    products = Product.objects.all()
    return render(request, "sale.html", {"products": products})