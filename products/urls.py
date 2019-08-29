from django.conf.urls import url, include
from .views import sale, view_product

urlpatterns = [
    url(r'^sale/$', sale, name='products'),
    url(r'^view_product/(?P<id>\d+)/$', view_product, name="view_product"),
]