from django.shortcuts import render

# Create your views here.
def get_tipsoftheweek(request):
    return render(request, 'firstaidtipsoftheweek.html')