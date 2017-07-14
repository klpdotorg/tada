from rest_framework import viewsets


from accounts.permissions import WorkUnderInstitutionPermission
from schools.serializers import TeacherSerializer
from schools.models import Teacher
from schools.filters import TeacherFilter


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = (WorkUnderInstitutionPermission, )
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_class = TeacherFilter
