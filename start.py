import os
from colorama import init, Fore, Back

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

MEAL_DATA = {
    1: {
        "type": "Breakfast",
        "sets": {
            1: {"name": "Set-A: Egg and Hotdog", "price": 50},
            2: {"name": "Set-B: Egg and Hungarian", "price": 60},
            3: {"name": "Set-C: Egg and Ham", "price": 70},
        },
    },
    2: {
        "type": "Lunch",
        "sets": {
            1: {"name": "Set-A: Adobo", "price": 60},
            2: {"name": "Set-B: Sinigang", "price": 80},
            3: {"name": "Set-C: Putchero", "price": 40},
        },
    },
    3: {
        "type": "Dinner",
        "sets": {
            1: {"name": "Set-A: Paksiw", "price": 60},
            2: {"name": "Set-B: Torta", "price": 80},
            3: {"name": "Set-C: Nilaga", "price": 40},
        },
    },
}

def display_meal_types():
    for key, value in MEAL_DATA.items():
        print(Fore.RED + f"{key}. " + Fore.RESET + value["type"])

def display_meal_sets(meal_type):
    sets = MEAL_DATA[meal_type]["sets"]
    for key, value in sets.items():
        print(Fore.RED + f"{key}.", Fore.RESET + value["name"], "-", Fore.BLUE + f"₱{value['price']}" + Fore.RESET)

def get_valid_integer(prompt, options=None):
    while True:
        try:
            value = int(input(prompt))
            if options and value not in options:
                raise ValueError(f"Invalid option! Please choose from {options}.")
            return value
        except ValueError as e:
            print(Fore.RED + str(e) + Fore.RESET)

def get_valid_payment(prompt, total_price):
    while True:
        try:
            payment = float(input(prompt))
            if payment < total_price:
                raise ValueError(f"Insufficient payment. You still owe ₱{total_price - payment:.2f}.")
            return payment
        except ValueError as e:
            print(Fore.RED + str(e) + Fore.RESET)

def main():
    while True:
        clear_screen()
        print(Fore.YELLOW + "\n----------------------------------------" + Fore.RESET)
        print(Back.RED + "\t MEAL RESERVATION PROGRAM " + Back.RESET)
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

        name = input("Name: ")
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

        display_meal_types()
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
        meal_type = get_valid_integer("Meal (1, 2, or 3): ", options=list(MEAL_DATA.keys()))

        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
        display_meal_sets(meal_type)
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

        meal_set = get_valid_integer("Meal-Set (1, 2, or 3): ", options=MEAL_DATA[meal_type]["sets"].keys())
        selected_set = MEAL_DATA[meal_type]["sets"][meal_set]

        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
        num_adult = get_valid_integer("Number of Adult/s: ")
        num_kid = get_valid_integer("Number of Kid's (50% Discount): ")
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

        total_price = selected_set["price"] * (num_adult + num_kid * 0.5)

        print(Back.RED + "\t CUSTOMER COPY: RECEIPT " + Back.RESET)
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
        print(f"Name: {name}")
        print(f"Meal: {MEAL_DATA[meal_type]['type']}")
        print(f"Meal Set: {selected_set['name']}")
        print(f"Number of Adult/s: {num_adult}")
        print(f"Number of Kid/s (50% Discount): {num_kid}")
        print(f"Total number of Reservation: {num_adult + num_kid}")
        print(f"Total Price: ₱{total_price:.2f}")
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

        payment = get_valid_payment("Payment: ₱", total_price)
        change = payment - total_price
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
        print(Back.RED + f" Change: ₱{change:.2f} " + Back.RESET)
        print(Fore.YELLOW + "----------------------------------------\n" + Fore.RESET)

        while True:
            again = input(Fore.GREEN + "Would you like to order again? (y/n): " + Fore.RESET).lower()
            if again in ['y', 'n']:
                break
            else:
                print(Fore.RED + "Invalid input! Please enter 'y' for yes or 'n' for no." + Fore.RESET)
        if again == 'n':
            print(Fore.YELLOW + "\n----------------------------------------\n" + Fore.RESET)
            print(Fore.GREEN + "Thank you for using the Program!" + Fore.RESET)
            print(Fore.YELLOW + "\n----------------------------------------\n" + Fore.RESET)
            break

if __name__ == "__main__":
    main()
