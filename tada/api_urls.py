from django.conf.urls import patterns, url

from schools.api_views import (
    InstitutionDetailView, StudentDetailView
)

urlpatterns = patterns(
    '',
    url('^institution/(?P<pk>[0-9]+)$', InstitutionDetailView.as_view(), name='api_institution_detail_view'),
    url('^student/(?P<pk>[0-9]+)$', StudentDetailView.as_view(), name='api_student_detail_view'),

)
