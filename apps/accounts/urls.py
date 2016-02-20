from django.conf.urls import patterns, include, url
from django.contrib import admin

from accounts.views import UserView

urlpatterns = patterns(
    '',
    url(r'^me/$', UserView.as_view(), name='user'),
    url(r'^', include('djoser.urls.authtoken')),
)
