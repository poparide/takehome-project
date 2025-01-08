from rest_framework import serializers

from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = (
            "origin",
            "destination",
            "departure_time",
            "state",
            "creator",
            "num_seats_available",
        )
