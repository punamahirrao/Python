def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F.")
