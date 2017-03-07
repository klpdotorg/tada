from rest_framework import permissions
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import Group

from schools.models import Boundary


class AssessmentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.has_perm('change_assessment', obj)


class HasAssignPermPermission(BasePermission):
    def has_permission(self, request, view):
        GROUPS_ALLOWED = [u'tada_admin',u'tada_dee']
        groups = Group.objects.filter(name__in=GROUPS_ALLOWED)

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        elif not request.user.groups.filter(id__in=groups).exists():
            return False
        else:
            return True


class InstitutionPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.has_perm('change_institution', obj)

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        elif request.method == 'POST':
             boundary_id = request.data.get('boundary', None)
             try:
                 boundary = Boundary.objects.get(id=boundary_id)
             except:
                 return False
             return request.user.has_perm('add_institution', boundary)
        else:
            return True
