from django.conf import settings
from django.test import TestCase
from airplane.tests.factories import AirplaneFactory
from math import log as logarithm


class TestAirplane(TestCase):

    def setUp(self):
        self.airplane_consumption = settings.AIRPLANE_FUEL_CONSUMPTION_PER_MINUTE_COEFFICIENT
        self.passanger_consumption = settings.PASSENGER_FUEL_CONSUMPTION_PER_MINUTE_COEFFICIENT
        self.airplane_capacity = settings.AIRPLANE_FUEL_TANK_CAPACITY_COEFFICIENT

        self.airplane_1 = AirplaneFactory(airplane_id=1, passengers_count=200)
        self.airplane_2 = AirplaneFactory(airplane_id=2, passengers_count=100)

    def test_fuel_consumption_per_minute(self):
        self.assertEqual(self.airplane_1.fuel_consumption_per_minute,
                         logarithm(1) * self.airplane_consumption + self.passanger_consumption * self.airplane_1.passengers_count)
        self.assertEqual(self.airplane_2.fuel_consumption_per_minute,
                         logarithm(2) * self.airplane_consumption + self.passanger_consumption * self.airplane_2.passengers_count)

    def test_flight_limit_minutes(self):
        self.assertEqual(self.airplane_1.flight_limit_minutes,
                         1 * self.airplane_capacity/(logarithm(1) * self.airplane_consumption + self.passanger_consumption * 200))
        self.assertEqual(self.airplane_2.flight_limit_minutes,
                         2 * self.airplane_capacity/(logarithm(2) * self.airplane_consumption + self.passanger_consumption * 100))
