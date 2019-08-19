from django.conf.urls import url, include
from .views import sale

urlpatterns = [
    url(r'^sale/', sale, name='products'),
]