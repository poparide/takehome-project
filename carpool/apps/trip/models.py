from django.contrib.auth.models import User
from django.db import models


class Trip(models.Model):
    """
    Trip from A to B at time
    """

    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

    STATE_CHOICES = [
        (OPEN, "Open"),
        (CLOSED, "Closed"),
        (CANCELLED, "Cancelled"),
    ]

    origin = models.ForeignKey(
        "location.Location", on_delete=models.PROTECT, related_name="trips_from"
    )
    destination = models.ForeignKey(
        "location.Location", on_delete=models.PROTECT, related_name="trips_to"
    )

    departure_time = models.DateTimeField()

    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=OPEN)

    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trips_created"
    )

    num_seats_available = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Trip from {self.origin} to {self.destination} on {self.departure_time}"
