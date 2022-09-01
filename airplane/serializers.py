from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    fuel_consumption_per_minute = serializers.SerializerMethodField(
        source='get_fuel_consumption_per_minute'
    )
    flight_limit_minutes = serializers.SerializerMethodField(
        source='get_flight_limit_minutes'
    )

    class Meta:
        model = Airplane
        fields = (
            'user_id',
            'airplane_id',
            'passengers_count',
            'fuel_consumption_per_minute',
            'flight_limit_minutes',
        )
        read_only_fields = ('user_id',)

    @staticmethod
    def get_fuel_consumption_per_minute(obj) -> float:
        return obj.fuel_consumption_per_minute

    @staticmethod
    def get_flight_limit_minutes(obj) -> float:
        return obj.flight_limit_minutes
