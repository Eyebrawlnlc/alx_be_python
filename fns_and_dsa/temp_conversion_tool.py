unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
temperature = float(input("Enter the temperature value: "))

def convert_to_celsius(fahrenheit):
    if unit.upper() != 'F':
        raise ValueError("Unit must be Fahrenheit (F) for this conversion.")
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0/9.0

def convert_to_fahrenheit(celsius):
    if unit.upper() != 'C':
        raise ValueError("Unit must be Celsius (C) for this conversion.")
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0/5.0) + 32

print(f"Converted temperature: {convert_to_celsius(temperature) if unit.upper() == 'F' else convert_to_fahrenheit(temperature)}")