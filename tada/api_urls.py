from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter

from django.conf.urls import patterns, url

from schools.api_views import (
    BoundaryViewSet,
    BoundaryTypeViewSet,
    BoundaryCategoryViewSet,
    InstitutionViewSet,
    InstitutionAssessmentViewSet,
    ProgrammeViewSet,
    StaffViewSet,
    StudentViewSet,
    StudentAssessmentViewSet,
)

router = routers.SimpleRouter()
bulkrouter = BulkRouter()
bulkrouter.register(r'students', StudentViewSet, base_name='students')

router.register(
    r'institution-assessments',
    InstitutionAssessmentViewSet,
    base_name='institution-assessment'
)
router.register(r'boundaries', BoundaryViewSet, base_name='boundary')
router.register(r'boundarytypes', BoundaryTypeViewSet, base_name='boundarytype')
router.register(r'boundarycategories', BoundaryCategoryViewSet, base_name='boundarycategory')
router.register(r'institutions', InstitutionViewSet, base_name='institution')
router.register(r'programmes', ProgrammeViewSet, base_name='programme')
router.register(r'staff', StaffViewSet, base_name='staff')
router.register(
    r'student-assessments',
    StudentAssessmentViewSet,
    base_name='student-assessment'
)
#router.register(r'students', StudentViewSet, base_name='students')
urlpatterns = router.urls + bulkrouter.urls
