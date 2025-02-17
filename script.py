# script.py
def length_converter():
    print("Length converter functionality")

def weight_converter():
    print("Weight converter functionality")

def temperature_converter():
    print("Temperature converter functionality")

# Instead of asking for user input, use a predefined choice
main_choice = 1  # Predefined value (e.g., length converter)

if main_choice == 1:
    length_converter()
elif main_choice == 2:
    weight_converter()
elif main_choice == 3:
    temperature_converter()
else:
    print("Invalid choice")
