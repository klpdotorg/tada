from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from guardian.shortcuts import get_objects_for_user

from schools.models import Boundary

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    group = serializers.CharField(write_only=True, allow_blank=True)
    groups = GroupSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User._meta.pk.name,
            User.USERNAME_FIELD,
            'group',
            'groups',
            'first_name',
            'last_name',
            'permissions',
        )
        read_only_fields = (
            User.USERNAME_FIELD,
            'groups'
        )

    def update(self, instance, validated_data):
        user = instance
        group_name = validated_data.pop('group', None)

        if group_name:
            try:
                user.groups.clear()
                group = Group.objects.get(name=group_name)
                group.user_set.add(user)
            except:
                raise ValidationError(group_name + " not found.")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def get_permissions(self, obj):
        user = obj
        response = {}

        response['assessments'] = get_objects_for_user(
            user, "schools.change_assessment"
        ).values_list('id', flat=True)

        response['boundaries'] = get_objects_for_user(
            user, "add_institution", klass=Boundary
        ).values_list('id', flat=True)

        response['institutions'] = get_objects_for_user(
            user, "schools.change_institution"
        ).values_list('id', flat=True)

        return response

