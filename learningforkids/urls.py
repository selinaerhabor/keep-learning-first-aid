from django.conf.urls import url
from learningforkids.views import learningforkids, learningforkidsquiz

urlpatterns = [
    url(r'^kids_home/$', learningforkids, name="learningforkids"),
    url(r'^kids_quiz/$', learningforkidsquiz, name="learningforkidsquiz")
]