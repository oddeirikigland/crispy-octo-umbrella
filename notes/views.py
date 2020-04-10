from rest_framework import viewsets, permissions

from notes.serializers import NotesSerializer
from notes.models import Note


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticated]
