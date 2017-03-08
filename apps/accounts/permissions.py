from rest_framework import permissions
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import Group

from schools.models import Boundary, Institution, StudentGroup


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


class StudentGroupPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.has_perm('change_studentgroup', obj)

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        elif request.method == 'POST':
            institution_id = request.data.get('institution', None)
            try:
                institution = Institution.objects.get(id=institution_id)
            except:
                return False
            return request.user.has_perm('add_studentgroup', institution)
        else:
            return True


class StudentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.has_perm('change_student', obj)

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        elif request.method == 'POST':
            studentgroup_id = view.kwargs.get('parent_lookup_studentgroups', None)
            institution_id = view.kwargs.get('parent_lookup_studentgroups__institution', None)
            try:
                if institution_id:
                    institution = Institution.objects.get(id=institution_id)
                elif studentgroup_id:
                    studentgroup = StudentGroup.objects.get(id=studentgroup_id)
                    institution = studentgroup.institution
                else:
                    return False
            except:
                return False
            return request.user.has_perm('add_student', institution)
        else:
            return True


class StaffPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.has_perm('change_staff', obj)

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        elif request.method == 'POST':
            institution_id = request.data.get('institution', None)
            try:
                institution = Institution.objects.get(id=institution_id)
            except:
                return False
            return request.user.has_perm('add_staff', institution)
        else:
            return True
