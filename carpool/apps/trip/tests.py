from django.test import TestCase
from django.urls import reverse
from apps.trip.models import Trip
from apps.trip.serializers import TripSerializer

from rest_framework.test import APIClient

class TripListTestCase(TestCase):
    fixtures = ["users", "locations", "trips"]
    client_class = APIClient

    def setUp(self):
       self.trip = Trip.objects.get()

    def test_trip_list_ok(self):
        response = self.client.get(
            reverse("trip_list")
        )
        self.assertEqual(
            response.json()[0], TripSerializer(self.trip).data
        )
