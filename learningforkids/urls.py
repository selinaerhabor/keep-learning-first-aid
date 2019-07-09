from django.conf.urls import url
from learningforkids.views import learningforkids, quiz

urlpatterns = [
    url(r'^learningforkids/$', learningforkids, name="learningforkids"),
    url(r'^quiz/$', quiz, name="quiz")
]