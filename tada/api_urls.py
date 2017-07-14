from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from django.conf.urls import patterns, url

from schools.api_views import (
    AssessmentViewSet,
    AnswerStudentViewSet,
    AnswerStudentGroupViewSet,
    AnswerInstitutionViewSet,
    AssessmentListViewSet,
    BoundaryViewSet,
    BoundaryCategoryViewSet,
    BoundaryTypeViewSet,
    InstitutionViewSet,
    InstitutionCategoryViewSet,
    InstitutionManagementViewSet,
    LanguageViewSet,
    ProgrammeViewSet,
    QuestionViewSet,
    StaffViewSet,
    StudentViewSet,
    StudentGroupViewSet,
    StudentStudentGroupViewSet,
    AssessmentStudentGroupAssociationViewSet,
    AssessmentInstitutionAssociationViewSet,
    TeacherViewSet,
    SearchKLPViewSet
)

bulkrouter = BulkRouter()
router = routers.SimpleRouter()
nested_router = ExtendedSimpleRouter()

router.register(r'assessments', AssessmentListViewSet, base_name='list_assessment')
router.register(r'boundaries', BoundaryViewSet, base_name='boundary')
router.register(r'boundarycategories', BoundaryCategoryViewSet, base_name='boundarycategory')
router.register(r'boundarytypes', BoundaryTypeViewSet, base_name='boundarytype')
router.register(r'institutioncategories', InstitutionCategoryViewSet, base_name='institutiocategory')
router.register(r'institutionmanagements', InstitutionManagementViewSet, base_name='institutiomanagement')
router.register(r'languages', LanguageViewSet, base_name='language')
router.register(r'staff', StaffViewSet, base_name='staff')
router.register(r'teacher', TeacherViewSet, base_name='teacher')
router.register(r'searchklp', SearchKLPViewSet, base_name='searchklp')

router.register(r'assessmentinstitutionmap', AssessmentInstitutionAssociationViewSet, base_name='assessmentinstitutionmap')

router.register(r'assessmentstudentgroupmap', AssessmentStudentGroupAssociationViewSet, base_name='assessmentstudentgroupnmap')

bulkrouter.register(r'students', StudentViewSet, base_name='students')

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

## Programmes -> Assessments -> Students -> AnswerStudent
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
            r'students',
            StudentViewSet,
            base_name='student',
            parents_query_lookups=['assessment__programme', 'assessment']
            ).register(
                r'answers',
                AnswerStudentViewSet,
                base_name='answer_student',
                parents_query_lookups=[
                    'student__studentgroup__asssessment__programme',
                    'student__studentgroup__asssessment',
                    'student']
            )

## Programmes -> Assessments -> Institutions -> AnswerInstitution
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
            r'institutions',
            InstitutionViewSet,
            base_name='institution',
            parents_query_lookups=[
                'assessmentinstitutionassociation__assessment__programme',
                'assessmentinstitutionassociation__assessment']
            ).register(
                r'answers',
                AnswerInstitutionViewSet,
                base_name='answer_institution',
                parents_query_lookups=[
                    'institution__assessmentinstitutionassociation__assessment__programme',
                    'institution__assessmentinstitutionassociation__assessment',
                    'institution']
            )

## Programmes -> Assessments -> StudentGroups -> AnswerStudentGroup
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
            r'studentgroups',
            StudentGroupViewSet,
            base_name='studentgroup',
            parents_query_lookups=[
                'assessmentstudentgroupassociation__assessment__programme',
                'assessmentstudentgroupassociation__assessment']
            ).register(
                r'answers',
                AnswerStudentGroupViewSet,
                base_name='answer_studentgroup',
                parents_query_lookups=[
                    'studentgroup__assessmentstudentgroupassociation__assessment__programme',
                    'studentgroup__assessmentstudentgroupassociation__assessment',
                    'studentgroup']
            )

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

urlpatterns = router.urls + bulkrouter.urls + nested_router.urls
