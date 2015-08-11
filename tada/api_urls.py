from rest_framework import routers

from django.conf.urls import patterns, url

from schools.api_views import (
    InstitutionViewSet, StudentDetailView, StudentsListView,
    AssessmentViewSet, ProgrammeViewSet, BoundaryViewSet
)

router = routers.SimpleRouter()

router.register(r'institutions', InstitutionViewSet, base_name='institution')
router.register(r'assessments', AssessmentViewSet, base_name='assessment')
router.register(r'programmes', ProgrammeViewSet, base_name='programme')
router.register(r'boundaries', BoundaryViewSet, base_name='boundary')

urlpatterns = patterns(
    '',
    url('^student/(?P<pk>[0-9]+)$', StudentDetailView.as_view(), name='api_student_detail_view'),
    url('^students/', StudentsListView.as_view(), name='api_students_list_view'),

) + router.urls
