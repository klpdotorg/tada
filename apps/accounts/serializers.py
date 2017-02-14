from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):

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
        )
        read_only_fields = (
            User.USERNAME_FIELD,
            'groups'
        )

    def update(self, instance, validated_data):
        group_name = validated_data.pop('group', None)

        if group_name:
            try:
                group = Group.objects.get(name=group_name)
                group.user_set.add(instance)
            except:
                raise ValidationError(group_name + " not found.")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
