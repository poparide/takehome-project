from apps.location.models import Location
from django.contrib import admin


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    ...
