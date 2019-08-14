from django.conf.urls import url
from learningforkids.views import learningforkids, kidsquiz

urlpatterns = [
    url(r'^learningforkids/$', learningforkids, name="learningforkids"),
    url(r'^kidsquiz/$', kidsquiz, name="kidsquiz")
]