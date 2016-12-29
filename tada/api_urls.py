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
    StudentStudentGroupViewSet,
)

bulkrouter = BulkRouter()
router = routers.SimpleRouter()
nested_router = ExtendedSimpleRouter()

router.register(r'boundaries', BoundaryViewSet, base_name='boundary')
router.register(r'boundarycategories', BoundaryCategoryViewSet, base_name='boundarycategory')
router.register(r'boundarytypes', BoundaryTypeViewSet, base_name='boundarytype')

## Institution -> StudentGroup -> Students
nested_router.register(
    r'institutions',
    InstitutionViewSet,
    base_name='institution'
    ).register(
        r'studentgroups',
        StudentGroupViewSet,
        base_name='studentgroup',
        parents_query_lookups=['institution']
        ).register(
            r'students',
            StudentViewSet,
            base_name='nested_students',
            parents_query_lookups=['studentgroups__institution', 'studentgroups']
        )

router.register(r'languages', LanguageViewSet, base_name='language')

## Programmes -> Assessments -> Questions
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

router.register(r'staff', StaffViewSet, base_name='staff')

## StudentGroups -> Students -> StudentStudentGroupRelation
nested_router.register(
    r'studentgroups',
    StudentGroupViewSet,
    base_name='studentgroup',
    ).register(
        r'students',
        StudentViewSet,
        base_name='nested_students',
        parents_query_lookups=['studentgroups']
        ).register(
            r'enrollment',
            StudentStudentGroupViewSet,
            base_name='studentstudentgrouprelation',
            parents_query_lookups=['student__studentgroups', 'student']
        )

##  Students -> StudentGroups -> StudentStudentGroupRelation
nested_router.register(
    r'students',
    StudentViewSet,
    base_name='students',
    ).register(
        r'studentgroups',
        StudentGroupViewSet,
        base_name='nested_students',
        parents_query_lookups=['students']
        ).register(
            r'enrollment',
            StudentStudentGroupViewSet,
            base_name='studentstudentgrouprelation',
            parents_query_lookups=['student_id', 'student_group']
        )

#http://localhost:8000/api/v1/studentgroups/3525154/students/2294002/enrollment

bulkrouter.register(r'students', StudentViewSet, base_name='students')

urlpatterns = router.urls + bulkrouter.urls + nested_router.urls
