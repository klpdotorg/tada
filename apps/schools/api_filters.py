import django_filters

from schools.models import Boundary

class BoundaryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        name="boundary_category__boundary_category"
    )

    class Meta:
        model = Boundary
        fields = ['category', 'boundary_type', 'parent']
