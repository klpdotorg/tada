from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    InstitutionSerializer,
)

from .models import (
    Institution,
)


class InstitutionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstitutionSerializer

    def get_object(self):
        return Institution.objects.get(id=self.kwargs['pk'])