from django.urls import path

from apps.trip.views import TripListView

urlpatterns = [
    path("", TripListView.as_view(), name="trip_list"),
]
