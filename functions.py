def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # Step 7: this is correct

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    # Step 11: handle extreme low temperatures
    if fahrenheit < -459.67:  # Absolute zero in Fahrenheit
        raise ValueError("Temperature below absolute zero!")
    return multiply(subtract(fahrenheit, 32), 5 / 9)

