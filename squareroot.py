import math

def calculate_sqrt(number):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(number)
