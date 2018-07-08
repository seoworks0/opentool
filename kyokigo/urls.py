from django.conf.urls import url
from django.contrib import admin
from .views import PostList, kyokifunc
from django.urls import path, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^kyokifunc$', kyokifunc, name='kyokifunc'),
]
