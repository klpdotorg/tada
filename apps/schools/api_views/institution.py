from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from schools.filters import (
    AssessmentFilter,
    BoundaryFilter,
    InstitutionFilter,
    ProgrammeFilter,
    QuestionFilter
)

from schools.serializers import (
    AssessmentSerializer,
    BoundarySerializer,
    BoundaryCategorySerializer,
    BoundaryTypeSerializer,
    InstitutionSerializer,
    ProgrammeSerializer,
    QuestionSerializer,
    StaffSerializer,
)

from schools.models import (
    Assessment,
    Boundary,
    BoundaryCategory,
    BoundaryType,
    Institution,
    Programme,
    Question,
    Staff,
)


class AssessmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class BoundaryViewSet(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer
    filter_class = BoundaryFilter


class BoundaryCategoryViewSet(viewsets.ModelViewSet):
    queryset = BoundaryCategory.objects.all()
    serializer_class = BoundaryCategorySerializer


class BoundaryTypeViewSet(viewsets.ModelViewSet):
    queryset = BoundaryType.objects.all()
    serializer_class = BoundaryTypeSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_class = InstitutionFilter


class ProgrammeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    filter_class = ProgrammeFilter


class QuestionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

