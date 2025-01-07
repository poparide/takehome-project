from rest_framework.generics import ListAPIView
from .models import Trip
from .serializers import TripSerializer


class TripListView(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
