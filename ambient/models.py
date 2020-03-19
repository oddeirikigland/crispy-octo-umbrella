from django.db import models
from django.conf import settings
from django.dispatch import receiver
from rest_framework import authentication, authtoken


class BearerAuthentication(authentication.TokenAuthentication):
    keyword = "Bearer"


@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        authtoken.models.Token.objects.create(user=instance)


class Face(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

