from rest_framework.permissions import BasePermission
from django.contrib.auth import Group


class HasAssignPermPermission(BasePermission):
    def has_permission(self, request, view):
        GROUPS_ALLOWED = [u'tada_admin',u'tada_dee']
        groups = Group.objects.filter(name__in=GROUPS_ALLOWED)
        if not user.groups.filter(id__in=groups).exists():
            return False

        return True
        
