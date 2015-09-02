from rest_framework import routers

from django.conf.urls import patterns, url

from schools.api_views import (
    InstitutionViewSet, StudentsListViewSet, StaffViewSet,
    AssessmentViewSet, ProgrammeViewSet, BoundaryViewSet
)

router = routers.SimpleRouter()

router.register(r'institutions', InstitutionViewSet, base_name='institution')
router.register(r'assessments', AssessmentViewSet, base_name='assessment')
router.register(r'programmes', ProgrammeViewSet, base_name='programme')
router.register(r'boundaries', BoundaryViewSet, base_name='boundary')
router.register(r'students', StudentsListViewSet, base_name='students')
router.register(r'staff',StaffViewSet, base_name='staff')
urlpatterns = router.urls
