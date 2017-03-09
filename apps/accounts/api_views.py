from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from guardian.shortcuts import (
    assign_perm,
    get_objects_for_user,
    remove_perm
)

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .filters import UserFilter
from .serializers import GroupSerializer, UserSerializer
from .permissions import HasAssignPermPermission

from schools.models import (
    Assessment,
    Boundary,
    BoundaryCategory,
    Institution,
)

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        password = request.data.get('password', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if password:
            instance.set_password(password)
            instance.save()

        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionView(APIView):
    permission_classes = (HasAssignPermPermission,)

    def assign_institution_permissions(self, user_to_be_permitted, institution_id):
        try:
            institution = Institution.objects.get(id=institution_id)
        except Exception as ex:
            raise APIException(ex)
        assign_perm('change_institution', user_to_be_permitted, institution)
        assign_perm('add_studentgroup', user_to_be_permitted, institution)
        assign_perm('add_student', user_to_be_permitted, institution)
        assign_perm('add_staff', user_to_be_permitted, institution)
        for staff in institution.staff_set.all():
            assign_perm('change_staff', user_to_be_permitted, staff)
            for studentgroup in institution.studentgroup_set.all():
                assign_perm('change_studentgroup', user_to_be_permitted, studentgroup)
                for student in studentgroup.students.all():
                    assign_perm('change_student', user_to_be_permitted, student)

    def assign_boundary_permissions(self, user_to_be_permitted, boundary_id):
        try:
            boundary = Boundary.objects.get(id=boundary_id)
        except Exception as ex:
            raise APIException(ex)

        institutions_under_boundary = boundary.get_institutions()
        for institution in institutions_under_boundary:
            self.assign_institution_permissions(user_to_be_permitted, institution.id)

        child_clusters = boundary.get_clusters()
        for cluster in child_clusters:
            assign_perm('add_institution', user_to_be_permitted, cluster)

    def assign_assessment_permissions(self, user_to_be_permitted, assessment_id):
        try:
            assessment = Assessment.objects.get(id=assessment_id)
        except Exception as ex:
            raise APIException(ex)
        assign_perm('change_assessment', user_to_be_permitted, assessment)

    def unassign_institution_permissions(self, user_to_be_denied, institution_id):
        try:
            institution = Institution.objects.get(id=institution_id)
        except Exception as ex:
            raise APIException(ex)
        remove_perm('change_institution', user_to_be_denied, institution)
        remove_perm('add_studentgroup', user_to_be_denied, institution)
        remove_perm('add_student', user_to_be_denied, institution)
        remove_perm('add_staff', user_to_be_denied, institution)
        for staff in institution.staff_set.all():
            remove_perm('change_staff', user_to_be_denied, staff)
            for studentgroup in institution.studentgroup_set.all():
                remove_perm('change_studentgroup', user_to_be_denied, studentgroup)
                for student in studentgroup.students.all():
                    remove_perm('change_student', user_to_be_denied, student)

    def unassign_boundary_permissions(self, user_to_be_denied, boundary_id):
        try:
            boundary = Boundary.objects.get(id=boundary_id)
        except Exception as ex:
            raise APIException(ex)

        institutions_under_boundary = boundary.get_institutions()
        for institution in institutions_under_boundary:
            self.unassign_institution_permissions(user_to_be_denied, institution.id)

        child_clusters = boundary.get_clusters()
        for cluster in child_clusters:
            remove_perm('add_institution', user_to_be_denied, cluster)

    def unassign_assessment_permissions(self, user_to_be_denied, assessment_id):
        try:
            assessment = Assessment.objects.get(id=assessment_id)
        except Exception as ex:
            raise APIException(ex)
        remove_perm('change_assessment', user_to_be_denied, assessment)

    def get(self, request, pk):
        try:
            permitted_user = User.objects.get(id=pk)
        except Exception as ex:
            raise APIException(ex)

        response = {}

        response['assessments'] = get_objects_for_user(
            permitted_user, "schools.change_assessment"
        ).values_list('id', flat=True)

        response['boundaries'] = get_objects_for_user(
            permitted_user, "schools.change_boundary"
        ).values_list('id', flat=True)

        response['institutions'] = get_objects_for_user(
            permitted_user, "schools.change_institution"
        ).values_list('id', flat=True)

        return Response(response)

    def post(self, request, pk):
        institution_id = self.request.data.get('institution_id', None)
        boundary_id = self.request.data.get('boundary_id', None)
        assessment_id = self.request.data.get('assesment_id', None)

        try:
            user_to_be_permitted = User.objects.get(id=pk)
        except Exception as ex:
            raise APIException(ex)

        if institution_id:
            self.assign_institution_permissions(user_to_be_permitted, institution_id)

        if assessment_id:
            self.assign_assessment_permissions(user_to_be_permitted, assessment_id)

        if boundary_id:
            self.assign_boundary_permissions(user_to_be_permitted, boundary_id)

        return Response("Permissions assigned")

    def delete(self, request, pk):
        institution_id = self.request.data.get('institution_id', None)
        boundary_id = self.request.data.get('boundary_id', None)
        assessment_id = self.request.data.get('assesment_id', None)

        try:
            user_to_be_denied = User.objects.get(id=pk)
        except Exception as ex:
            raise APIException(ex)

        if institution_id:
            self.unassign_institution_permissions(user_to_be_denied, institution_id)

        if assessment_id:
            self.unassign_assessment_permissions(user_to_be_denied, assessment_id)

        if boundary_id:
            self.unassign_boundary_permissions(user_to_be_denied, boundary_id)

        return Response("Permissions unassigned")

