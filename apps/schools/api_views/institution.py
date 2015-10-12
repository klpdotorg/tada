from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from schools.filters import (
    BoundaryFilter, ProgrammeFilter, AssessmentFilter,
    InstitutionFilter,
)
from schools.serializers import (
    InstitutionSerializer, AssessmentSerializer, ProgrammeSerializer,
    BoundarySerializer, BoundaryTypeSerializer,StaffSerializer,
    BoundaryCategorySerializer
)
from schools.models import (
    Institution, AssessmentInstitution, ProgrammeInstitution,
    Boundary, BoundaryType, Staff, BoundaryCategory
)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_class = InstitutionFilter


class AssessmentInstitutionViewSet(viewsets.ModelViewSet):
    queryset = AssessmentInstitution.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = ProgrammeInstitution.objects.all()
    serializer_class = ProgrammeSerializer
    filter_class = ProgrammeFilter


class BoundaryViewSet(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer
    filter_class = BoundaryFilter


class BoundaryTypeViewSet(viewsets.ModelViewSet):
    queryset = BoundaryType.objects.all()
    serializer_class = BoundaryTypeSerializer


class BoundaryCategoryViewSet(viewsets.ModelViewSet):
    queryset = BoundaryCategory.objects.all()
    serializer_class = BoundaryCategorySerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

