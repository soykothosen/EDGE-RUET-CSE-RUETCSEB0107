# Celsius to Fahrenheit Converter

try:
    # Get user input for temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Display the result
    print(f"{celsius}°C is equal to {fahrenheit}°F")
except ValueError:
    print("Invalid input. Please enter a valid number.")
