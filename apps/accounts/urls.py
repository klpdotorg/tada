from django.conf.urls import patterns, include, url
from django.contrib import admin

from accounts.api_views import UserViewSet

ListCreateMapper = {
    'get' : 'list',
    # 'post' : 'create',
}

RetrieveUpdateDestroyMapper = {
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy',
}

urlpatterns = patterns(
    '',
    url(
        r'^users/$',
        UserViewSet.as_view(ListCreateMapper),
        name='users_list_create'
    ),
    url(
        r'^users/(?P<pk>[0-9]+)/$',
        UserViewSet.as_view(RetrieveUpdateDestroyMapper),
        name='users_detail'
    ),
    url(r'^', include('djoser.urls.authtoken')),
)
