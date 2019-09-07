from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Product

# Create your views here.
def do_search(request):
    products = Product.objects.filter(category__icontains=request.GET['q'])
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
