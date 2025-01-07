from django.contrib import admin
from apps.trip.models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    ...