from django.conf.urls import patterns, include, url
from django.contrib import admin

from .api_views import (
    PermissionView,
    ReportView,
    UserViewSet,
    LoginView,
)

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
    url(
        r'^users/(?P<pk>[0-9]+)/reports/$',
        ReportView.as_view(),
        name='reports_view'
    ),
    url(
        r'^users/(?P<pk>[0-9]+)/permissions/$',
        PermissionView.as_view(),
        name='permissions_view'
    ),
    url(
        r'^users/(?P<user_pk>[0-9]+)/permissions/(?P<permission_pk>[0-9]+)/$',
        PermissionView.as_view(),
        name='permissions_view'
    ),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^', include('djoser.urls.authtoken')),
)
