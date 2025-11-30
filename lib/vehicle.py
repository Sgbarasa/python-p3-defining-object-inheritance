#!/usr/bin/env python3

class Vehicle:
    """Represents a generic vehicle."""

    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        """Return the vehicle's driving sound."""
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        """Return the refueling message."""
        return "filling up!"
