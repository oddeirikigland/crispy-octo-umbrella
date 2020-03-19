from django.contrib.auth.models import User, Group
from rest_framework import serializers

from ambient.models import Face


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class FaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Face
        fields = ["created", "description"]
