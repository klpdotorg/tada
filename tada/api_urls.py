from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

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
    QuestionInstitutionViewSet,
    QuestionStudentViewSet,
    StaffViewSet,
    StudentViewSet,
    StudentGroupViewSet,
)

from accounts.api_views import (
    UserViewSet,
    GroupViewSet,
)

router = routers.SimpleRouter()
bulkrouter = BulkRouter()
nested_router = ExtendedSimpleRouter()

bulkrouter.register(r'students', StudentViewSet, base_name='students')

router.register(
    r'users',
    UserViewSet,
    base_name='user'
)
router.register(
    r'groups',
    GroupViewSet,
    base_name='user'
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
    r'programmes-institution',
    ProgrammeInstitutionViewSet,
    base_name='programme-institution'
).register(
    r'assessments-institution',
    AssessmentInstitutionViewSet,
    base_name='assessment-institution',
    parents_query_lookups=['programme']
).register(
    r'questions-institution',
    QuestionInstitutionViewSet,
    base_name='question-institution',
    parents_query_lookups=['assessment__programme', 'assessment']
)

nested_router.register(
    r'programmes-student',
    ProgrammeStudentViewSet,
    base_name='programme-student'
).register(
    r'assessments-student',
    AssessmentStudentViewSet,
    base_name='assessment-student',
    parents_query_lookups=['programme']
).register(
    r'questions-student',
    QuestionStudentViewSet,
    base_name='question-student',
    parents_query_lookups=['assessment__programme', 'assessment']
)

router.register(
    r'staff',
    StaffViewSet,
    base_name='staff'
)

#router.register(r'students', StudentViewSet, base_name='students')
urlpatterns = router.urls + bulkrouter.urls + nested_router.urls
