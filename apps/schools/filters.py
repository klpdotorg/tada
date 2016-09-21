import django_filters

from schools.models import (
    AssessmentInstitution,
    AssessmentStudent,
    Boundary,
    Institution,
    ProgrammeInstitution,
    ProgrammeStudent,
    QuestionInstitution,
    Student,
    StudentGroup
)


class BoundaryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        name="boundary_category__boundary_category"
    )

    class Meta:
        model = Boundary
        fields = ['category', 'boundary_type', 'parent']


class ProgrammeInstitutionFilter(django_filters.FilterSet):

    class Meta:
        model = ProgrammeInstitution
        fields = ['name']


class ProgrammeStudentFilter(django_filters.FilterSet):

    class Meta:
        model = ProgrammeStudent
        fields = ['name']


class QuestionFilter(django_filters.FilterSet):

    class Meta:
        model = QuestionInstitution
        fields = ['name']


class AssessmentInstitutionFilter(django_filters.FilterSet):

    class Meta:
        model = AssessmentInstitution
        fields = ['name']


class AssessmentStudentFilter(django_filters.FilterSet):

    class Meta:
        model = AssessmentStudent
        fields = ['name']


class InstitutionFilter(django_filters.FilterSet):

    class Meta:
        model = Institution
        fields = ['name', 'boundary']


class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name']

class StudentGroupFilter(django_filters.FilterSet):

    class Meta:
        model = StudentGroup
        fields = ['name', 'section', 'active', 'group_type']
