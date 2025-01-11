def temp_conversion_tool():
  """Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors."""

  # Define global conversion factors
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
  CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

  def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

  def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

  # User interaction
  while True:
    try:
      temperature_value = float(input("Enter a temperature value: "))
      temperature_unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

      if temperature_unit == "C":
        converted_temperature = convert_to_fahrenheit(temperature_value)
        temperature_unit = "F"
      elif temperature_unit == "F":
        converted_temperature = convert_to_celsius(temperature_value)
        temperature_unit = "C"
      else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

      print(f"{temperature_value:.2f} {temperature_unit} is equivalent to {converted_temperature:.2f} degrees Celsius.")
      break

    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  temp_conversion_tool()