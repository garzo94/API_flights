from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields='__all__'

    def validate_flightNumer(self, flightNumber):
        # print('###############################')
        # print(re.match("",""))
        if (re.match("^[a-zA-Z0-9]*$", flightNumber)==None):
               raise serializers.ValidationError("invalid number")
        return flightNumber

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields='__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'
