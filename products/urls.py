from django.conf.urls import url, include
from .views import sale, view_product, get_books, get_ebooks, get_posters, get_extras, get_cds, get_courses, get_firstaidkits, get_manikins

urlpatterns = [
    url(r'^sale/$', sale, name='sale'),
    url(r'^view_product/(?P<id>\d+)/$', view_product, name="view_product"),
    url(r'^sale/books/$', get_books, name="get_books"),
    url(r'^sale/ebooks/$', get_ebooks, name="get_ebooks"),
    url(r'^sale/posters/$', get_posters, name="get_posters"),
    url(r'^sale/extras/$', get_extras, name="get_extras"),
    url(r'^sale/cds/$', get_cds, name="get_cds"),
    url(r'^sale/courses/$', get_courses, name="get_courses"),
    url(r'^sale/firstaidkits/$', get_firstaidkits, name="get_firstaidkits"),
    url(r'^sale/manikins/$', get_manikins, name="get_manikins"),
]