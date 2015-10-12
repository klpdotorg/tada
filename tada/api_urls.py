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
    ProgrammeInstitutionViewSet,
    ProgrammeStudentViewSet,
    StaffViewSet,
    StudentViewSet,
)

router = routers.SimpleRouter()
bulkrouter = BulkRouter()
bulkrouter.register(r'students', StudentViewSet, base_name='students')

router.register(
    r'assessments-institution',
    AssessmentInstitutionViewSet,
    base_name='assessment-institution'
)
router.register(
    r'assessments-student',
    AssessmentStudentViewSet,
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
    r'programmes-institution',
    ProgrammeInstitutionViewSet,
    base_name='programme-institution'
)
router.register(
    r'programmes-student',
    ProgrammeStudentViewSet,
    base_name='programme-student'
)
router.register(
    r'staff',
    StaffViewSet,
    base_name='staff'
)

#router.register(r'students', StudentViewSet, base_name='students')
urlpatterns = router.urls + bulkrouter.urls
