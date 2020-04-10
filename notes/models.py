from django.db import models


class Note(models.Model):
    person = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.person
