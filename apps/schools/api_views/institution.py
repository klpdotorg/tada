from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from accounts.permissions import (
    AssessmentPermission,
    InstitutionPermission,
    StaffPermission,
)

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
    InstitutionCategorySerializer,
    InstitutionManagementSerializer,
    LanguageSerializer,
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
    InstitutionCategory,
    InstitutionManagement,
    MoiType,
    Programme,
    Question,
    Staff,
)


class AssessmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (AssessmentPermission,)
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
    permission_classes = (InstitutionPermission,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_class = InstitutionFilter


class InstitutionCategoryViewSet(viewsets.ModelViewSet):
    queryset = InstitutionCategory.objects.all()
    serializer_class = InstitutionCategorySerializer


class InstitutionManagementViewSet(viewsets.ModelViewSet):
    queryset = InstitutionManagement.objects.all()
    serializer_class = InstitutionManagementSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = MoiType.objects.all()
    serializer_class = LanguageSerializer


class ProgrammeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    filter_class = ProgrammeFilter


class QuestionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter


class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = (StaffPermission,)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

