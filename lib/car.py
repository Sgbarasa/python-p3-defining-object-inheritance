#!/usr/bin/env python3

from vehicle import Vehicle

class Car(Vehicle):
    """Represents a car, which is a type of Vehicle."""

    def go(self):
        """Return the car's driving sound."""
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
