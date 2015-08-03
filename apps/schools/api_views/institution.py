from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from schools.serializers import (
    InstitutionSerializer, AssessmentSerializer, ProgrammeSerializer,
    BoundarySerializer
)
from schools.models import (
    Institution, AssessmentInstitution, ProgrammeInstitution,
    Boundary
)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = AssessmentInstitution.objects.all()
    serializer_class = AssessmentSerializer


class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = ProgrammeInstitution.objects.all()
    serializer_class = ProgrammeSerializer


class BoundaryViewSet(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        category = request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(
                boundary_category__boundary_category=category
            )

        boundary_type_id = request.query_params.get('boundary_type_id', None)
        if boundary_type_id:
            queryset = queryset.filter(
                boundary_type=boundary_type_id
            )

        parent_id = request.query_params.get('parent_id', None)
        if parent_id:
            queryset = queryset.filter(
                parent=parent_id
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
