from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model

from guardian.shortcuts import get_objects_for_user

from schools.models import Assessment, Boundary

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    permissions = serializers.SerializerMethodField()
    group = serializers.CharField(write_only=True, allow_blank=True)

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
            'is_active',
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
            user, "crud_answers", klass=Assessment
        ).values_list('id', flat=True)

        response['boundaries'] = get_objects_for_user(
            user, "add_institution", klass=Boundary
        ).values_list('id', flat=True)

        response['institutions'] = get_objects_for_user(
            user, "schools.change_institution"
        ).values_list('id', flat=True)

        return response

    def get_groups(self, obj):
        user = obj
        groups = user.groups.all().values('name')
        if user.is_superuser:
            groups = [{'name':'tada_admin'}]
        return groups


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=False, style={'input_type': 'password'})

    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.'),
    }

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.user = None
        self.fields[User.USERNAME_FIELD] = serializers.CharField(required=False)

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get(User.USERNAME_FIELD), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = (
            'auth_token',
        )
