from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^user/$', user_profile, name="user_profile"),
    url(r'^password_reset/', include(url_reset))
]