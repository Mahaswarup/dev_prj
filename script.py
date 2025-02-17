def length_converter():
    print("\nLength Conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} km = {km * 0.621371} miles")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles = {miles * 1.60934} km")
    else:
        print("Invalid choice")

def weight_converter():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kg = {kg * 2.20462} pounds")
    elif choice == '2':
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} pounds = {pounds * 0.453592} kg")
    else:
        print("Invalid choice")

def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {(celsius * 9/5) + 32}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5/9}°C")
    else:
        print("Invalid choice")

print("Unit Converter")
print("1. Length Converter")
print("2. Weight Converter")
print("3. Temperature Converter")

main_choice = input("Enter choice (1/2/3): ")

if main_choice == '1':
    length_converter()
elif main_choice == '2':
    weight_converter()
elif main_choice == '3':
    temperature_converter()
else:
    print("Invalid choice")
