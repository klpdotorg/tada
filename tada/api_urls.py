from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter

from django.conf.urls import patterns, url

from schools.api_views import (
    AssessmentInstitutionViewSet,
    AssessmentStudentViewSet,
    BoundaryViewSet,
    BoundaryCategoryViewSet,
    BoundaryTypeViewSet,
    InstitutionViewSet,
    ProgrammeViewSet,
    StaffViewSet,
    StudentViewSet,
)

router = routers.SimpleRouter()
bulkrouter = BulkRouter()
bulkrouter.register(r'students', StudentViewSet, base_name='students')

router.register(
    r'assessments-institution',
    InstitutionAssessmentViewSet,
    base_name='assessment-institution'
)
router.register(
    r'assessments-student',
    StudentAssessmentViewSet,
    base_name='assessment-student'
)
router.register(
    r'boundaries',
    BoundaryViewSet,
    base_name='boundary'
)
router.register(
    r'boundarycategories',
    BoundaryCategoryViewSet,
    base_name='boundarycategory'
)
router.register(
    r'boundarytypes',
    BoundaryTypeViewSet,
    base_name='boundarytype'
)
router.register(
    r'institutions',
    InstitutionViewSet,
    base_name='institution'
)
router.register(
    r'programmes',
    ProgrammeViewSet,
    base_name='programme'
)
router.register(
    r'staff',
    StaffViewSet,
    base_name='staff'
)

#router.register(r'students', StudentViewSet, base_name='students')
urlpatterns = router.urls + bulkrouter.urls
