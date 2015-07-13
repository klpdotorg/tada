from django.conf.urls import patterns, url

from schools.api_views import (
    InstitutionDetailView, StudentDetailView, StudentsListView
)

from schools.models import (
    Student,
)

from schools.serializers import (
    StudentSerializer,
)

urlpatterns = patterns(
    '',
    url('^institution/(?P<pk>[0-9]+)$', InstitutionDetailView.as_view(), name='api_institution_detail_view'),
    url('^student/(?P<pk>[0-9]+)$', StudentDetailView.as_view(), name='api_student_detail_view'),
    url('^students/', StudentsListView.as_view(), name='api_students_list_view'),

)
