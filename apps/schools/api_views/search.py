from rest_framework import viewsets
from rest_framework.response import Response


from schools.models import Institution, Student
from schools.serializers import InstitutionSerializer, StudentSerializer
from accounts.permissions import WorkUnderInstitutionPermission


class SearchKLPViewSet(viewsets.ViewSet):
    permission_classes = (WorkUnderInstitutionPermission, )

    def list(self, request):
        klp_id = request.GET.get('klp_id', 0)
        institutions = Institution.objects.filter(
            id__contains=klp_id, active=2)[:3]
        students = Student.objects.filter(
            id__contains=klp_id, active=2)[:3]
        return Response({
            'institutions': InstitutionSerializer(
                institutions, many=True).data,
            'students': StudentSerializer(students, many=True).data
        })
