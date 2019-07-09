from django.shortcuts import render

# Create your views here.
def sale(request):
    return render(request, 'sale.html')