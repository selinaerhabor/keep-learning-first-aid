from django.shortcuts import render
from products.models import Product

# Displays Homepage
def home(request):
    products = Product.objects.filter(featured_page="H")
    return render(request, 'index.html', {"products": products})
    
# Displays FAQs page
def faqs(request):
    return render(request, 'faqs.html')