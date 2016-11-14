from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from django.conf.urls import patterns, url

from schools.api_views import (
    AssessmentViewSet,
    BoundaryViewSet,
    BoundaryCategoryViewSet,
    BoundaryTypeViewSet,
    InstitutionViewSet,
    LanguageViewSet,
    ProgrammeViewSet,
    QuestionViewSet,
    StaffViewSet,
    StudentViewSet,
    StudentGroupViewSet,
)

router = routers.SimpleRouter()
bulkrouter = BulkRouter()
nested_router = ExtendedSimpleRouter()

bulkrouter.register(r'students', StudentViewSet, base_name='students')

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

# Nested Routers

nested_router.register(
    r'institutions',
    InstitutionViewSet,
    base_name='institution'
).register(
    r'studentgroups',
    StudentGroupViewSet,
    base_name='studentgroup',
    parents_query_lookups=['institution']
)

nested_router.register(
    r'programmes',
    ProgrammeViewSet,
    base_name='programme'
).register(
    r'assessments',
    AssessmentViewSet,
    base_name='assessment',
    parents_query_lookups=['programme']
).register(
    r'questions',
    QuestionViewSet,
    base_name='question',
    parents_query_lookups=['assessment__programme', 'assessment']
)

router.register(
    r'staff',
    StaffViewSet,
    base_name='staff'
)

router.register(
    r'languages',
    LanguageViewSet,
    base_name='language'
)

#router.register(r'students', StudentViewSet, base_name='students')
urlpatterns = router.urls + bulkrouter.urls + nested_router.urls
