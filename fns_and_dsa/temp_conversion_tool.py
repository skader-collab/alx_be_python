# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature():
    """Prompts the user to input a valid numeric temperature."""
    while True:
        try:
            temp_input = float(input("Enter the temperature: ").strip())
            return temp_input
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_unit():
    """Prompts the user to input a valid unit (C or F)."""
    while True:
        unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit): ").strip().upper()
        if unit in ('C', 'F'):
            return unit
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def display_conversion(temp, unit):
    """Displays the converted temperature based on the unit provided."""
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp:.2f}°C is equivalent to {converted_temp:.2f}°F.")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp:.2f}°F is equivalent to {converted_temp:.2f}°C.")

def main():
    """Main function to interact with the user and perform temperature conversions."""
    temp = get_temperature()
    unit = get_unit()
    display_conversion(temp, unit)

if __name__ == "__main__":
    main()
