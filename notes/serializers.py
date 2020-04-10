from rest_framework import serializers

from .models import Note


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ("person", "notes")
