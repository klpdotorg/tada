from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_bulk import BulkCreateModelMixin, ListBulkCreateUpdateDestroyAPIView

from accounts.permissions import WorkUnderInstitutionPermission

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
    permission_classes = (WorkUnderInstitutionPermission,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_class = StudentFilter

    # M2M query returns duplicates. Overrode this function
    # from NestedViewSetMixin to implement the .distinct()
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
    permission_classes = (WorkUnderInstitutionPermission,)
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    filter_class = StudentGroupFilter

    # M2M query returns duplicates. Overrode this function
    # from NestedViewSetMixin to implement the .distinct()
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


class StudentStudentGroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = StudentStudentGroupRelation.objects.all()
    serializer_class = StudentStudentGroupSerializer

    # M2M query returns duplicates. Overrode this function
    # from NestedViewSetMixin to implement the .distinct()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = 0
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

