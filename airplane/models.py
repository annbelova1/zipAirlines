from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

from math import log as logarithm


class Airplane(models.Model):
    user_id = models.PositiveIntegerField(null=True)
    passengers_count = models.PositiveIntegerField(default=0)
    airplane_id = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created = models.DateTimeField(verbose_name="created", help_text="date of creation", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="updated", help_text="profile updated", auto_now=True)

    class Meta:
        verbose_name = "Airplane"
        verbose_name_plural = "Airplanes"
        ordering = ("-created",)

    def __str__(self) -> str:
        return f'Airplane {self.airplane_id} with {self.passengers_count} passengers, user: {self.user_id}'

    @property
    def fuel_consumption_per_minute(self) -> float:
        return (
            (logarithm(self.airplane_id) * settings.AIRPLANE_FUEL_CONSUMPTION_PER_MINUTE_COEFFICIENT)
            + (self.passengers_count * settings.PASSENGER_FUEL_CONSUMPTION_PER_MINUTE_COEFFICIENT)
        )

    @property
    def flight_limit_minutes(self) -> float:
        return (
            self.airplane_id * settings.AIRPLANE_FUEL_TANK_CAPACITY_COEFFICIENT/self.fuel_consumption_per_minute
            if self.fuel_consumption_per_minute != 0
            else 0
        )
