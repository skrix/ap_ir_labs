"""
Module car: Defines classes related to car specifications and behavior.
"""

from enum import Enum
from dataclasses import dataclass
from datetime import datetime

class CarBrand(Enum):
    """Enumeration for car brands."""
    ACURA = "Acura"
    ALFA_ROMEO = "Alfa Romeo"
    ASTON_MARTIN = "Aston Martin"
    AUDI = "Audi"
    BMW = "BMW"
    CHEVROLET = "Chevrolet"
    DODGE = "Dodge"
    FIAT = "Fiat"
    FORD = "Ford"
    HONDA = "Honda"
    HYUNDAI = "Hyundai"
    INFINITI = "Infiniti"
    JAGUAR = "Jaguar"
    JEEP = "Jeep"
    KIA = "Kia"
    LAMBORGHINI = "Lamborghini"
    LAND_ROVER = "Land Rover"
    LEXUS = "Lexus"
    MAZDA = "Mazda"
    MERCEDES_BENZ = "Mercedes-Benz"
    MITSUBISHI = "Mitsubishi"
    NISSAN = "Nissan"
    PEUGEOT = "Peugeot"
    PORSCHE = "Porsche"
    RENAULT = "Renault"
    SEAT = "Seat"
    SKODA = "Skoda"
    SUBARU = "Subaru"
    SUZUKI = "Suzuki"
    TOYOTA = "Toyota"
    VOLKSWAGEN = "Volkswagen"
    VOLVO = "Volvo"

class FuelType(Enum):
    """Enumeration for fuel types."""
    PETROL = "Petrol"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"

class EngineType(Enum):
    """Enumeration for engine types."""
    I4 = "Inline 4"
    V6 = "V6"
    V8 = "V8"
    V12 = "V12"

class CarAlreadyParkedException(Exception):
    """Exception raised when a car is already parked."""

class CarNotParkedException(Exception):
    """Exception raised when a car is not parked but tried to leave."""

@dataclass
class CarEngine:
    """Represents a car engine with volume, type, fuel, horse power, and top speed."""

    def __init__(self, engine_spec: dict):
        """
        Initialize a CarEngine with engine specifications.

        engine_spec (dict): 'volume', 'engine_type', 'fuel', 'horse_power', 'top_speed'.
        """
        self.volume = engine_spec['volume']
        self.engine_type = engine_spec['engine_type']
        self.fuel = engine_spec['fuel']
        self.horse_power = engine_spec['horse_power']
        self.top_speed = engine_spec['top_speed']

    def __str__(self):
        """String representation of the CarEngine."""
        return (f"{self.engine_type.value}, {self.volume}cc, {self.horse_power}HP, "
                f"{self.top_speed}KM/h, Fuel: {self.fuel.value}")

class Car:
    """Represents a car with make, model, year, plate number, and engine."""

    def __init__(self, car_spec: dict):
        """
        Initialize a Car with car specifications.

        car_spec (dict): 'make', 'model', 'year', 'plate_number', 'engine'.
        """
        self.make = car_spec['make']
        self.model = car_spec['model']
        self.year = car_spec['year']
        self.engine = car_spec['engine']
        self.plate_number = car_spec['plate_number']
        self.parked_at = None

    def parking_duration(self):
        """Calculate how long the car has been parked (in hours)."""
        if self.parked_at is None:
            return 0
        return round((datetime.now() - self.parked_at).total_seconds() / 3600.0, 2)

    def park(self):
        """Mark the car as parked by setting the current time."""
        if self.parked_at is not None:
            raise CarAlreadyParkedException('Car already parked!')

        self.parked_at = datetime.now()

    def leave(self):
        """Calculate the duration the car has been parked and reset parked_at."""
        if self.parked_at is None:
            raise CarNotParkedException('Car not parked!')
        duration = self.parking_duration()
        self.parked_at = None
        return duration
