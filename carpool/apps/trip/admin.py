from apps.trip.models import Trip
from django.contrib import admin


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    ...
