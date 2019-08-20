"""keeplearningfirstaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import home, faqs
from firstaidtipsoftheweek.views import firstaidtipsoftheweek
from learningforkids.views import learningforkids, learningforkidsquiz
from learningforadults.views import learningforadults
from accounts import urls
from products.views import sale
from products import urls
from cart import urls
from search import urls
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^firstaidtipsoftheweek/$', firstaidtipsoftheweek, name="firstaidtipsoftheweek"),
    url(r'^learningforkids/$', learningforkids, name="learningforkids"),
    url(r'^learningforkidsquiz/$', learningforkidsquiz, name="learningforkidsquiz"),
    # url(r'^learningforkids/', include('learningforkids.urls')),
    url(r'^learningforadults/$', learningforadults, name="learningforadults"),
    url(r'^faqs/$', faqs, name="faqs"),
    url(r'^sale/$', sale, name="sale"),
    url(r'^sale/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^cart/', include('search.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]