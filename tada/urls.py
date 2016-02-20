from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^auth/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('tada.api_urls')),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
)
