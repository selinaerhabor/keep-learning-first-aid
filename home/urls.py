from django.conf.urls import url
from .views import home, faqs, thanks

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^faqs/', faqs, name='faqs'),
    url(r'^thanks/', thanks, name='thanks'),
]