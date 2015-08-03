from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from schools.serializers import (
    InstitutionSerializer,
)
from schools.models import (
    Institution,
)

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
