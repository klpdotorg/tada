from django.http import Http404

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
    StudentGroupSerializer,
    StudentStudentGroupSerializer
)
from schools.models import (
    Student,
    StudentGroup,
    StudentStudentGroupRelation
)


class StudentViewSet(NestedViewSetMixin, BulkCreateModelMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_class = StudentFilter

    def filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict:
            try:
                return queryset.filter(
                    **parents_query_dict
                ).order_by().distinct('id')
            except ValueError:
                raise Http404
        else:
            return queryset


class StudentGroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    filter_class = StudentGroupFilter
