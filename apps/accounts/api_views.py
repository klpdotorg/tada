from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from guardian.shortcuts import assign_perm

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


class AssignPermissionView(APIView):
    permission_classes = (HasAssignPermPermission,)
    
    def post(self, request):
        user_id = self.request.data.get('user_id', None)
        institution_id = self.request.data.get('institution_id', None)
        boundary_id = self.request.data.get('boundary_id', None)
        assessment_id = self.request.data.get('assesment_id', None)

        try:
            user_to_be_permitted = User.objects.get(id=user_id)
        except Exception as ex:
            raise APIException(ex)

        if institution_id:
            try:
                institution = Institution.objects.get(id=institution_id)
            except Exception as ex:
                raise APIException(ex)
            assign_perm('change_institution', user_to_be_permitted, institution)

        if assessment_id:
            try:
                assessment = Assessment.objects.get(id=assessment_id)
            except Exception as ex:
                raise APIException(ex)
            assign_perm('change_assessment', user_to_be_permitted, assessment)

        if boundary_id:
            try:
                boundary = Boundary.objects.get(id=boundary_id)
            except Exception as ex:
                raise APIException(ex)
            assign_perm('change_boundary', user_to_be_permitted, boundary)

            institutions_under_boundary = boundary.institutions()
            for institution in institutions_under_boundary:
                assign_perm('change_institution', user_to_be_permitted, institution)

            child_boundaries = boundary.children()
            for boundary in child_boundaries:
                assign_perm('change_boundary', user_to_be_permitted, boundary)

        return Response("Permissions assigned")
