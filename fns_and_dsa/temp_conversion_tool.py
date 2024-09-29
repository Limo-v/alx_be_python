CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    temperature = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'{fahrenheit}°F is {temperature}°C')
def convert_to_fahrenheit(celsius):
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f'{celsius}°C is {temperature}°F')

temperature =  float(input("Enter the temperature to convert:"))
measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()

match measurement:
    case "C":
        convert_to_fahrenheit(temperature)
    case "F":
        convert_to_celsius(temperature)