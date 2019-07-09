from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def faqs(request):
    return render(request, 'faqs.html')