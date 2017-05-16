import json
import arrow

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status, generics, viewsets, permissions

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .reports import Report
from .filters import UserFilter
from .utils import login_user, send_email
from .mixins import ActionViewMixin, PermissionMixin
from .permissions import HasAssignPermPermission, UserPermission
from .serializers import (
    GroupSerializer,
    UserSerializer,
    LoginSerializer,
    TokenSerializer,
)

User = get_user_model()


class LoginView(ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to obtain user authentication token.
    """
    serializer_class = LoginSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def _action(self, serializer):
        token = login_user(self.request, serializer.user)
        token_serializer_class = TokenSerializer
        response = token_serializer_class(token).data
        response['user_id'] = serializer.user.id
        return Response(
            data=response,
            status=status.HTTP_200_OK,
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    permission_classes = (UserPermission,)

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


class PermissionView(APIView, PermissionMixin):
    permission_classes = (HasAssignPermPermission,)

    def get(self, request, pk):
        try:
            permitted_user = User.objects.get(id=pk)
        except Exception as ex:
            raise APIException(ex)

        response = {}

        response['assessments'] = self.get_permitted_entities(
            permitted_user, permission="crud_answers", klass="assessment"
        )

        response['boundaries'] = self.get_permitted_entities(
            permitted_user, permission="add_institution", klass="boundary"
        )

        response['institutions'] = self.get_permitted_entities(
            permitted_user, permission="schools.change_institution"
        )

        return Response(response)

    def post(self, request, pk):
        institution_id = self.request.data.get('institution_id', None)
        boundary_id = self.request.data.get('boundary_id', None)
        assessment_id = self.request.data.get('assessment_id', None)

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
        assessment_id = self.request.data.get('assessment_id', None)

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


class ReportView(APIView):
    def get(self, request):
        from_date = request.query_params.get('from', None)
        to_date = request.query_params.get('to', None)
        to_email = request.query_params.get('to_email', None)

        if from_date:
            try:
                from_date = arrow.get(from_date, "YYYY-MM-DD").datetime
            except Exception as ex:
                raise APIException(ex)

        if to_date:
            try:
                to_date = arrow.get(to_date, "YYYY-MM-DD").datetime
            except Exception as ex:
                raise APIException(ex)

        report = Report(from_date, to_date)
        generated_report = report.generate()
        send_email(
            json.dumps(generated_report, indent=4),
            to_emails=to_email
        )
        return Response(generated_report)
