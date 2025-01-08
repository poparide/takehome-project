from apps.trip.views import TripListView
from django.urls import path

urlpatterns = [
    path("", TripListView.as_view(), name="trip_list"),
]
