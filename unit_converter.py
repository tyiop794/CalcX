"""
Unit Conversion by tyiop794

Convert any unit to any unit within range (make sure the units match [distance, volume, mass, temperature])
Should be able to convert floating numbers
Can export values over to a file or can be saved as a preset
Value can be saved to computer clipboard
Make interface?
Keep things simple; avoid redundant code wherever possible!
Test cases!!
Choose decimal place to round
Limit unit asking to a single function, avoiding redundancy
"""

import math

volume_units = ["ounces", "cups", "pints", "quarts", "gallons", "mililiters", "liters"]
distance_units = ["inches", "feet", "yards", "miles", "nanometers", "micrometers", "milimeters", "centimeters", "meters", "kilometers"]
mass_units = ["ounces", "pounds", "stones", "US tons", "micrograms", "miligrams", "grams", "kilograms", "metric tons"]
temp_units = ["\N{DEGREE FAHRENHEIT}", "\N{DEGREE CELSIUS}", "K"]
rounding_factor = 2
unit_types = [distance_units, mass_units, temp_units, volume_units]
presets = []
presets_units = []
measurements = ["distance", "mass", "temperature", "volume"] 
# Add changing rounding factor as an additional option
# Also allow presets to be added
measurement = 0 

def distance(unit, second_unit, amount):
    while unit != second_unit:
        if unit == 1:
            amount *= 12
            unit = 0
        if unit == 2:
            amount *= 36
            unit = 0
        if unit == 3:
            amount *= 63360
            unit = 0
        if unit == 0:
            if second_unit == 1:
                amount = amount / 12
                unit = second_unit
            elif second_unit == 2:
                amount = amount / 36
                unit = second_unit
            elif second_unit == 3:
                amount = amount / 63360
                unit = second_unit
            elif (second_unit >= 4 and second_unit <= 9):
                amount = amount * 0.0254
                unit = 8
            elif unit == 0:
                amount = amount
                unit = second_unit
    # Metric system
        if unit == 4:
            amount /= 1000000000
            unit = 8
        if unit == 5:
            amount /= 1000000
            unit = 8
        if unit == 6:
            amount /= 1000
            unit = 8
        if unit == 7:
            amount /= 100
            unit = 8
        if unit == 9:
            amount *= 1000
            unit = 8
        if unit == 8:
            if second_unit == 4:
                amount = amount * 1000000000 
                unit = second_unit
            elif second_unit == 5:
                amount = amount * 1000000
                unit = second_unit
            elif second_unit == 6:
                amount = amount * 1000
                unit = second_unit
            elif second_unit == 7:
                amount = amount * 100 
                unit = second_unit
            elif second_unit == 9:
                amount = amount / 1000
                unit = second_unit
            elif (second_unit >= 0 and second_unit <= 3):
                amount = amount * 39.37
                unit = 0
            elif second_unit == 8:
                amount = amount
                unit = second_unit
    return amount


def mass(unit, second_unit, amount):
    while unit != second_unit:
        if unit == 1:
            amount *= 16
            unit = 0
        if unit == 2:
            amount *= 224
            unit = 0
        if unit == 3:
            amount *= 32000
            unit = 0
        if unit == 0:
            if second_unit == 0:
                amount = amount
                unit = second_unit
            elif second_unit == 1:
                amount /= 16
                unit = second_unit
            elif second_unit == 2:
                amount /= 224
                unit = second_unit
            elif second_unit == 3:
                amount /= 32000
                unit = second_unit
            elif (second_unit >= 4 and second_unit <= 8):
                amount *= 28.3495
                unit = 6
        if unit == 4:
            amount /= 1000000
            unit = 6
        if unit == 5:
            amount /= 1000
            unit = 6
        if unit == 7:
            amount *= 1000
            unit = 6
        if unit == 8:
            amount *= 1000000
            unit = 6
        if unit == 6:
            if second_unit == 4:
                amount *= 1000000
                unit = second_unit
            elif second_unit == 5:
                amount *= 1000
                unit = second_unit
            elif second_unit == 6:
                amount = amount
                unit = second_unit
            elif second_unit == 7:
                amount /= 1000
                unit = second_unit
            elif second_unit == 8:
                amount /= 1000000
                unit = second_unit
            elif (second_unit >= 0 and second_unit <= 3):
                amount *= 0.035274
                unit = 0
        #amount = amount + " " + mass_units[unit] 
    return amount

def temp(unit, second_unit, amount):
    while unit != second_unit:
        if unit == 0:
            amount = (amount - 32) * (5/9)
            unit = 1
        if unit == 2:
            amount = (amount - 273.15)
            unit = 1
        if unit == 1:
            if second_unit == 0:
                amount = (amount * (9/5)) + 32
                unit = second_unit
            elif second_unit == 1:
                amount = amount
                unit = second_unit
            elif second_unit == 2:
                amount = (amount + 273.15)
                unit = second_unit
        #print(amount)
    return amount

def volume(unit, second_unit, amount):
    while unit != second_unit:
        if unit == 1:
            amount *= 8
            unit = 0 
        if unit == 2:
            amount *= 16
            unit = 0
        if unit == 3:
            amount *= 32
            unit = 0 
        if unit == 4:
            amount *= 128
            unit = 0
        if unit == 0:
            if second_unit == 1:
                amount /= 8
                unit = second_unit
            elif second_unit == 2:
                amount /= 16
                unit = second_unit
            elif second_unit == 3:
                amount /= 32
                unit = second_unit
            elif second_unit == 4:
                amount /= 128
                unit = second_unit
            elif (second_unit >= 5 or second_unit <= 6):
                amount /= 33.814
                unit = 6
            elif second_unit == 0:
                unit = second_unit
        if unit == 5:
            amount /= 1000
            unit = 6
        if unit == 6:
            if second_unit == 5:
                amount *= 1000
                unit = second_unit
            elif second_unit == 6:
                unit = second_unit
            elif (second_unit >= 0 or second_unit <= 4):
                amount *= 33.814
                unit = 0
    #amount = str(amount) + " " + volume_units[unit]
    #print(amount)
    return amount
                

