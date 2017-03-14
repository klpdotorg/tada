from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from guardian.shortcuts import assign_perm, get_users_with_perms

from accounts.permissions import (
    AssessmentPermission,
    InstitutionCreateUpdatePermission,
    WorkUnderInstitutionPermission,
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


class AssessmentListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


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
    permission_classes = (InstitutionCreateUpdatePermission,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_class = InstitutionFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self._assign_permissions(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def _assign_permissions(self, institution):
        users_to_be_permitted = get_users_with_perms(institution.boundary)
        for user_to_be_permitted in users_to_be_permitted:
            assign_perm('change_institution', user_to_be_permitted, institution)
            assign_perm('crud_student_class_staff', user_to_be_permitted, institution)


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
    permission_classes = (WorkUnderInstitutionPermission,)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

