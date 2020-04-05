from django.contrib import admin

from .models import PhoneBook

class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']

admin.site.register(PhoneBook, PhoneBookAdmin)
