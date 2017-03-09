from rest_framework import permissions
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import Group

from schools.models import Boundary, Institution, StudentGroup


class TadaBasePermission(BasePermission):
    def is_user_permitted(self, request):
        GROUPS_ALLOWED = [u'tada_admin']
        groups = Group.objects.filter(name__in=GROUPS_ALLOWED)

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        elif request.user.groups.filter(id__in=groups).exists():
            return True
        else:
            return False

    def has_permission(self, request, view):
        if self.is_user_permitted(request):
            return True
        else:
            return False


class AssessmentPermission(TadaBasePermission):
    def has_object_permission(self, request, view, obj):
        if self.is_user_permitted(request):
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


class InstitutionCreateUpdatePermission(TadaBasePermission):
    def has_object_permission(self, request, view, obj):
        if self.is_user_permitted(request):
            return True
        else:
            return request.user.has_perm('change_institution', obj)

    def has_permission(self, request, view):
        if self.is_user_permitted(request):
            return True
        elif request.method == 'POST':
            boundary_id = request.data.get('boundary', None)
            try:
                boundary = Boundary.objects.get(id=boundary_id)in
            except:
                return False
            return request.user.has_perm('add_institution', boundary)
        else:
            return True


class WorkUnderInstitutionPermission(TadaBasePermission):
    def has_permission(self, request, view):
        if self.is_user_permitted(request):
            return True
        else:
            institution_id = request.data.get('institution', None)
            try:
                institution = Institution.objects.get(id=institution_id)
            except:
                return False
        return request.user.has_perm('crud_student_class_staff', institution)
