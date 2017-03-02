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

    def _assign_permission(self, model_id, model_type):
        app_name = "schools"
        change_permission = "change_" + model_type

        try:
            if model_type == 'institution':
                obj = Institution.objects.get(id=model_id)
            elif model_type == 'assessment':
                obj = Assessment.objects.get(id=model_id)
            elif model_type == 'boundary':
                obj = Boundary.objects.get(id=model_id)
            else:
                raise APIException(
                    "Please specify an institution_id, assessment_id and / or boundary_id"
                )
        except Exception as ex:
            raise APIException(ex)

        assign_perm(change_permission, user_to_be_permitted, obj)

        return obj

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
            institution = self._assign_permission(
                user_to_be_permitted, institution_id, 'institution')

        if assessment_id:
            assessment = self._assign_permission(
                user_to_be_permitted, assessment_id, 'assessment')

        if boundary_id:
            boundary = self._assign_permission(
                user_to_be_permitted, boundary_id, 'boundary')

            # Give institution edit rights under the assigned boundary.
            institutions_under_boundary = boundary.get_institutions()
            for institution in institutions_under_boundary:
                assign_perm('change_institution', user_to_be_permitted, institution)

            # Give boundary edit rights for all boundaries under the parent one.
            child_boundaries = boundary.get_clusters()
            for boundary in child_boundaries:
                assign_perm('change_boundary', user_to_be_permitted, boundary)

        return Response("Permissions assigned")
