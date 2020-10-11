from django.contrib import admin
from .models import Service, Feature, Realtor, Static


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'number',)


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'email', 'phone',)



@admin.register(Static)
class StaticAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',)
