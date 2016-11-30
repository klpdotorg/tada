from rest_framework import serializers

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):

    groups = GroupSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User._meta.pk.name,
            User.USERNAME_FIELD,
            'groups',
            'first_name',
            'last_name',
        )
        read_only_fields = (
            User.USERNAME_FIELD,
        )
