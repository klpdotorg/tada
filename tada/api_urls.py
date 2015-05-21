from django.conf.urls import patterns, url

from schools.api_views import (
    InstitutionDetailView,
)

urlpatterns = patterns(
    '',
    url('^institution/(?P<pk>[0-9]+)$', InstitutionDetailView.as_view(), name='api_institution_detail_view'),
)
