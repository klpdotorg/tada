from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # home page
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('tada.api_urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^favicon\.ico$', 'django.views.static.serve', {
            'url': '/static/images/favicon.ico'
        }),
    )
