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
    AssessmentInstitution,
    AssessmentStudent,
    Boundary,
    BoundaryCategory,
    BoundaryType,
    Institution,
    ProgrammeInstitution,
    ProgrammeStudent,
    QuestionInstitution,
    QuestionStudent,
    Staff,
)


class AssessmentInstitutionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssessmentInstitution.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class AssessmentStudentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssessmentStudent.objects.all()
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


class ProgrammeInstitutionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ProgrammeInstitution.objects.all()
    serializer_class = ProgrammeSerializer
    filter_class = ProgrammeFilter


class ProgrammeStudentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ProgrammeStudent.objects.all()
    serializer_class = ProgrammeSerializer
    filter_class = ProgrammeFilter


class QuestionInstitutionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = QuestionInstitution.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter

class QuestionStudentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = QuestionStudent.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

