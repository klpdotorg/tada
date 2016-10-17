from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from accounts.serializers import (
    UserSerializer,
    GroupSerializer,
)

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        add_to_group_ids = request.data.pop('add_to_groups', [])
        remove_from_group_ids = request.data.pop('remove_from_groups', [])
        user = self.get_object()
        self.update_groups(
            user,
            add_to_group_ids,
            remove_from_group_ids
        )
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def update_groups(self, user, add_to_group_ids, remove_from_group_ids):
        try:
            groups = [
                Group.objects.get(id=group_id)
                for group_id in add_to_group_ids + remove_from_group_ids
            ]
        except:
            raise APIException('One or more of the given group IDs are invalid')

        if add_to_group_ids:
            for group in add_to_group_ids:
                user.groups.add(group)

        if remove_from_group_ids:
            for group in remove_from_group_ids:
                user.groups.remove(group)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
