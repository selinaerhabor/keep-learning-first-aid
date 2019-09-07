from django.conf.urls import url
from .views import firstaidtipsoftheweek

urlpatterns = [
    url(r'^this_week/$', firstaidtipsoftheweek, name='firstaidtipsoftheweek'),
]