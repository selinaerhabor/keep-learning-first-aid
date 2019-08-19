from django.conf.urls import url, include
from .views import tipoftheweek

urlpatterns = [
    url(r'^tipoftheweek/', tipoftheweek, name='firstaidtips'),
]