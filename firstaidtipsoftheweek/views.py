from django.shortcuts import render
from .models import Firstaidtip

# First Aid Tip of the Week
def firstaidtipsoftheweek(request):
    firstaidtips = Firstaidtip.objects.all()
    return render(request, "firstaidtipoftheweek.html", {"firstaidtips": firstaidtips})