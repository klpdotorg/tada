from rest_framework import viewsets
from rest_framework.response import Response


from accounts.permissions import WorkUnderInstitutionPermission
from schools.serializers import TeacherSerializer
from schools.models import Teacher
from schools.filters import TeacherFilter


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = (WorkUnderInstitutionPermission, )
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_class = TeacherFilter

    def list(self, request):
        queryset = Teacher.objects.filter(
            active=2,
            institution__pk=request.GET.get('institution', 0)
        )
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)
