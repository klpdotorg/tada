import django_filters

from schools.models import (
    Boundary, ProgrammeInstitution, AssessmentInstitution,
    Institution,
)


class BoundaryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        name="boundary_category__boundary_category"
    )

    class Meta:
        model = Boundary
        fields = ['category', 'boundary_type', 'parent']


class ProgrammeFilter(django_filters.FilterSet):

    class Meta:
        model = ProgrammeInstitution
        fields = ['name']


class AssessmentFilter(django_filters.FilterSet):

    class Meta:
        model = AssessmentInstitution
        fields = ['name']


class InstitutionFilter(django_filters.FilterSet):

    class Meta:
        model = Institution
        fields = ['name']
