from django.shortcuts import render
from .models import Firstaidtip
from datetime import datetime, timedelta
from django.utils import timezone

# First Aid Tip of the Week
def firstaidtipsoftheweek(request):
    firstaidtips = Firstaidtip.objects.filter(post_id="1")
    return render(request, "firstaidtipoftheweek.html", {"firstaidtips": firstaidtips})