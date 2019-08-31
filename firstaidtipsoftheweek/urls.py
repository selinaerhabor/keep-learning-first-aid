from django.conf.urls import url
from .views import firstaidtipsoftheweek

urlpatterns = [
    url(r'^firstaidtipoftheweek/$', firstaidtipsoftheweek, name='firstaidtipsoftheweek'),
]