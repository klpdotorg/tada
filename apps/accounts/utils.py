from django.contrib.auth import user_logged_in

from rest_framework import authtoken
from django.core.mail import EmailMultiAlternatives

def send_email(text_content, to_emails=None,
               from_email='tada@klp.org.in',
               subject='Tada Report'):

    if not to_emails:
        to_emails = ['dev@klp.org.in',]
    else:
        to_emails = [to_emails]

    try:
        msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    except Exception as ex:
        print ex
        return

    msg.send()

def login_user(request, user):
    token, _ = authtoken.models.Token.objects.get_or_create(user=user)
    user_logged_in.send(sender=user.__class__, request=request, user=user)
    return token
