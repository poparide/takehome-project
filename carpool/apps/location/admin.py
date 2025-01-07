from django.contrib import admin
from apps.location.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    ...