from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .filters import UserFilter
from .serializers import GroupSerializer, UserSerializer

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
    permission_classes = (permissions.HasAssignPermPermission,)
    
    def get(self, request):
        school_id = self.request.data.get('school_id', None)
        district_id = self.request.data.get('district_id', None)
        block_project_id = self.request.data.get('block_project_id', None)
        cluster_circle_id = self.request.data.get('cluster_circle_id', None)
        assessment_id = self.request.data.get('assesment_id', None)
        return Response("LOL!")
