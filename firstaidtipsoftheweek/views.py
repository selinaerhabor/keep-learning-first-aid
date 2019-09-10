from django.shortcuts import render
from .models import Firstaidtip
import datetime

# First Aid Tip of the Week
def firstaidtipsoftheweek(request):
    today = datetime.date.today()
    firstaidtips = Firstaidtip.objects.filter(startdate__lte = today, enddate__gte = today)
    return render(request, "firstaidtipoftheweek.html", {"firstaidtips": firstaidtips})
    
    