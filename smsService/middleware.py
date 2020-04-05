import json
import logging
import os

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv
from twilio.rest import Client
from .models import PhoneBook
from .serializers import PhoneBookSerializer

logger = logging.getLogger(__name__)


NOT_CONFIGURED_MESSAGE = (
    "Required enviroment variables "
    "TWILIO_ACCOUNT_SID or TWILIO_AUTH_TOKEN or TWILIO_NUMBER missing."
)


def load_admins_file():
    queryset = PhoneBook.objects.all()
    serializer_class = PhoneBookSerializer
    return queryset


def load_twilio_config():
    logger.debug("Loading Twilio configuration")

    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_number = os.getenv("TWILIO_NUMBER")

    if not all([twilio_account_sid, twilio_auth_token, twilio_number]):
        raise ImproperlyConfigured(NOT_CONFIGURED_MESSAGE)

    return (twilio_number, twilio_account_sid, twilio_auth_token)


class MessageClient:
    def __init__(self):
        logger.debug("Initializing messaging client")

        (twilio_number, twilio_account_sid, twilio_auth_token,) = load_twilio_config()

        self.twilio_number = twilio_number
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)

        logger.debug("Twilio client initialized")

    def send_message(self, body, to):
        self.twilio_client.messages.create(
            body=body,
            to=to,
            from_=self.twilio_number,
            # media_url=['https://demo.twilio.com/owl.png']
        )


class TwilioNotificationsMiddleware:
    def __init__(self):
        logger.debug("Initializing Twilio notifications middleware")

        self.contacts = load_admins_file()
        self.client = MessageClient()

        logger.debug("Twilio notifications middleware initialized")

    def process_message(self, message):
        for contact in self.contacts:
            message_to_send = message.format(contact.name)
            self.client.send_message(message_to_send, contact.phone_number)
        logger.info("Administrators notified!")
        return None
