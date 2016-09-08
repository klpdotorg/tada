from rest_framework import viewsets
from rest_framework.exceptions import APIException

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from accounts.serializers import (
    UserSerializer
)

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        group_ids = request.data.pop('groups', None)
        user = self.get_object()
        if group_ids:
            try:
                groups = [Group.objects.get(id=group_id) for group_id in group_ids]
            except:
                raise APIException('One or more of the given group IDs are invalid')
            for group in groups:
                user.groups.add(group)

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
