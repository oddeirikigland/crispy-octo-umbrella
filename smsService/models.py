from django.db import models

class PhoneBook(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.name
