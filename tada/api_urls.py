from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter

from django.conf.urls import patterns, url

from schools.api_views import (
    StaffViewSet,InstitutionViewSet, StudentViewSet,
    AssessmentViewSet, ProgrammeViewSet, BoundaryViewSet,
    BoundaryTypeViewSet, BoundaryCategoryViewSet
)

router = routers.SimpleRouter()
bulkrouter = BulkRouter()
bulkrouter.register(r'students', StudentViewSet, base_name='students')

router.register(r'assessments', AssessmentViewSet, base_name='assessment')
router.register(r'boundaries', BoundaryViewSet, base_name='boundary')
router.register(r'boundarytypes', BoundaryTypeViewSet, base_name='boundarytype')
router.register(r'boundarycategories', BoundaryCategoryViewSet, base_name='boundarycategory')
router.register(r'institutions', InstitutionViewSet, base_name='institution')
router.register(r'programmes', ProgrammeViewSet, base_name='programme')
router.register(r'staff', StaffViewSet, base_name='staff')
#router.register(r'students', StudentViewSet, base_name='students')
urlpatterns = router.urls + bulkrouter.urls
