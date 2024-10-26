"""
Module task_1_28: Defines a WaterPump class with details about brand, power, capacity, and model.
"""

import textwrap

class WaterPump:
    """
    WaterPump class to represent a pump with attributes for brand, wattage, capacity,
    model, serial, and manufacture year.
    """
    def __init__(self, brand=None, watt=None, capacity=None, model=None, serial=None, year=None):
        """
        Initialize a WaterPump object with brand, wattage,
        capacity, model, serial, and manufacture year.
        """
        self.__brand = brand
        self.__watt = watt
        self.__capacity = capacity
        self.model = model
        self.serial = serial
        self.year = year

    def get_brand(self):
        """Return the brand of the water pump."""
        return self.__brand

    def get_watt(self):
        """Return the wattage of the water pump."""
        return self.__watt

    def get_capacity(self):
        """Return the capacity of the water pump in liters per hour."""
        return self.__capacity

    def __str__(self):
        """Return a string representation of the WaterPump."""
        return f'WaterPump: {self.__brand}, {self.__watt} Watt, {self.__capacity} l/h'

    def __repr__(self):
        """Return a detailed string representation of the WaterPump for debugging."""
        return textwrap.dedent(f'''
        Record: WaterPump
        Brand: {self.__brand}
        Model: {self.model}
        Serial: {self.serial}
        Year: {self.year}
        Power: {self.__watt} watt
        Capacity: {self.__capacity} l/h
        ''')

    def __del__(self):
        """Handle object deletion by printing a message."""
        print(f"{self.__str__()} deleted.")


def main():
    """
    Create instances of the WaterPump class and print their detailed representations.
    """
    obj1 = WaterPump()
    obj2 = WaterPump('Bosch', 48, 996, 'Bosch Water Pump 16.6l / Minute 12V', 'BO-EWP004', 2024)
    obj3 = WaterPump('BGA', model='Water Pump Fiat Combo/Doblo/Ducato 1.6/2.0D/CDTi 10-',
                     serial='CP2660', year=2024)

    print(repr(obj1))
    print(repr(obj2))
    print(repr(obj3))

if __name__ == "__main__":
    main()
