from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PhoneBook
from .serializers import PhoneBookSerializer
from .middleware import TwilioNotificationsMiddleware

class PhoneBookViewSet(viewsets.ModelViewSet):
    queryset = PhoneBook.objects.all()
    serializer_class = PhoneBookSerializer

    @action(detail=False, url_path="dinner")
    def send_dinner_sms(self, request, pk=None):
        middleware = TwilioNotificationsMiddleware()
        middleware.process_message("""Dinner is ready, {0}! Hugs from your family <3 """)
        return Response()

    @action(detail=False, url_path="comehome")
    def send_comehome_sms(self, request, pk=None):
        middleware = TwilioNotificationsMiddleware()
        middleware.process_message("""It is time to come home, {0}! Hugs from your family <3 """)
        return Response()


    @action(detail=False, url_path="ishome")
    def send_ishome_sms(self, request, pk=None):
        middleware = TwilioNotificationsMiddleware()
        middleware.process_message("""A familymember just got home, {0}! Hugs from your family <3 """)
        return Response()
