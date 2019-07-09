from django.shortcuts import render

# Create your views here.
def tipsoftheweek(request):
    return render(request, 'firstaidtipsoftheweek.html')