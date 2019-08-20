from django.conf.urls import url
from learningforkids.views import learningforkids, learningforkidsquiz

urlpatterns = [
    url(r'^learningforkids/$', learningforkids, name="learningforkids"),
    url(r'^learningforkidsquiz/$', learningforkidsquiz, name="learningforkidsquiz")
]