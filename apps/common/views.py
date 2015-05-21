from rest_framework import generics
from rest_framework.views import APIView


class KLPAPIView(APIView):
    pass


class KLPListAPIView(generics.ListAPIView):
    pass


class KLPDetailAPIView(generics.RetrieveAPIView):
    pass
