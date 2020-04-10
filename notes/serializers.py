from rest_framework import serializers

from .models import Note


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ("person", "notes")

    def create(self, validated_data):
        person = validated_data.get("person", None)
        notes = validated_data.get("notes", None)
        if person is not None and notes is not None:
            person_exist = Note.objects.filter(person=person).update(notes=notes)
            if person_exist > 0:
                return Note.objects.filter(person=person).first()
        return Note.objects.create(**validated_data)
