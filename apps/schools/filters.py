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
        name="boundary_category__name"
    )

    class Meta:
        model = Boundary
        fields = ['category', 'boundary_type', 'parent']


class ProgrammeFilter(django_filters.FilterSet):
    boundary_type = django_filters.NumberFilter(
        name="programme_institution_category"
    )

    class Meta:
        model = Programme
        fields = ['name', 'active', 'boundary_type']


class QuestionFilter(django_filters.FilterSet):

    class Meta:
        model = Question
        fields = ['name']


class AssessmentFilter(django_filters.FilterSet):
    boundary = django_filters.NumberFilter(
        name="institutions__boundary"
    )

    class Meta:
        model = Assessment
        fields = ['name', 'boundary', 'active']


class InstitutionFilter(django_filters.FilterSet):

    class Meta:
        model = Institution
        fields = ['name', 'boundary']


class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'active']


class StudentGroupFilter(django_filters.FilterSet):

    class Meta:
        model = StudentGroup
        fields = ['name', 'section', 'active', 'group_type']
