from django.contrib.auth import user_logged_in

from rest_framework import authtoken


def login_user(request, user):
    token, _ = authtoken.models.Token.objects.get_or_create(user=user)
    user_logged_in.send(sender=user.__class__, request=request, user=user)
    return token


class ActionViewMixin(object):
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self._action(serializer)
