from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ComtactAdmin(admin.ModelAdmin):
    list_display = ('text', 'type',)
