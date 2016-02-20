from rest_framework import generics

from django.contrib.auth import get_user_model

from accounts.serializers import UserSerializer

User = get_user_model()


class UserView(generics.RetrieveUpdateAPIView):
    """
    Use this endpoint to retrieve/update user.
    """
    model = User
    serializer_class = UserSerializer

    def get_object(self, *args, **kwargs):
        return self.request.user
