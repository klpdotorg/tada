from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_bulk import BulkCreateModelMixin, ListBulkCreateUpdateDestroyAPIView

from schools.filters import (
    StudentFilter,
    StudentGroupFilter
)
from schools.serializers import (
    StudentSerializer,
    StudentGroupSerializer
)
from schools.models import (
    Student,
    StudentGroup
)


class StudentViewSet(BulkCreateModelMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_class = StudentFilter


class StudentGroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    filter_class = StudentGroupFilter
