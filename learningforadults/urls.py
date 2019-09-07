from django.conf.urls import url
from learningforadults.views import learningforadults, learningforadultsquiz

urlpatterns = [
    url(r'^adults/$', learningforadults, name="learningforadults"),
    url(r'^adults_quiz/$', learningforadultsquiz, name="learningforadultsquiz")
]