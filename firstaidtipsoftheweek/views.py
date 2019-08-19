from django.shortcuts import render
from .models import Firstaidtip

# Create your views here.
def tipoftheweek(request):
    firstaidtips = Firstaidtip.objects.all()
    return render(request, "firstaidtipoftheweek.html", {"firstaidtips": firstaidtips})