from django.conf.urls import url
from learningforadults.views import learningforadults, learningforadultsquiz

urlpatterns = [
    url(r'^learningforadults/$', learningforadults, name="learningforadults"),
    url(r'^learningforadultsquiz/$', learningforadultsquiz, name="learningforadultsquiz")
]