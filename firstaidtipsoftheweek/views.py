# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Firstaidtip

# Create your views here.
def firstaidtipsoftheweek(request):
    firstaidtips = Firstaidtip.objects.all()
    return render(request, "firstaidtipoftheweek.html", {"firstaidtips": firstaidtips})