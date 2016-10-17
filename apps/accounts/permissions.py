from rest_framework import permissions
from rest_framework.exceptions import APIException


class TadaPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user

        if user.is_superuser is True:
            return True

        if user.groups.filter(name="tada_admin").exists():
            return True

        if user.groups.filter(name="tada_deo"):
            return True

        if user.groups.filter(name="tada_dee"):
            return True
