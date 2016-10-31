import django_filters

from schools.models import (
    Assessment,
    Boundary,
    Institution,
    Programme,
    Question,
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
        model = Question
        fields = ['name']


class AssessmentFilter(django_filters.FilterSet):

    class Meta:
        model = Assessment
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
