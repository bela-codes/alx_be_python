# THIS ARE THE MULTIPLICATION FACTORS
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return fahrenheit

magnitude = int(input("Enter the magnitude: "))
user = input("Enter the unit of your measurement(Celsius(C), Fahrenheit(F)): ").lower()

if user == "c":
    converted_to_fahrenheit = convert_to_fahrenheit(magnitude)
    print(f"{magnitude}°C is {converted_to_fahrenheit}°F")
elif user == "f":
    converted_to_celsius = convert_to_celsius(magnitude)
    print(f"{magnitude}°F is {converted_to_celsius}°C")
else:
    print(f"please choose a valid option")
    