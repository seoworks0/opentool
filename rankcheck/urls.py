from django.conf.urls import url
from django.contrib import admin
from .views import PostList, rankfunc
from django.urls import path, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^rankfunc$', rankfunc, name='rankfunc'),
]
