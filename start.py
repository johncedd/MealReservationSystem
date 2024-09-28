import os
from colorama import init, Fore, Back, Style

init()

os.system('cls' if os.name == 'nt' else 'clear')

while True: 
    print(Fore.YELLOW + "\n----------------------------------------" + Fore.RESET)
    print(Back.RED + "\t MEAL RESERVATION PROGRAM " + Back.RESET)
    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    name = input("Name: ")
    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
    print(Fore.RED + "1. " + Fore.RESET + "Breakfast")
    print(Fore.RED + "2. " + Fore.RESET + "Lunch")
    print(Fore.RED + "3. " + Fore.RESET + "Dinner")
    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    while True:
        try:
            mType = int(input("Meal: "))
            if mType in [1, 2, 3]:
                break
            else:
                print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
                print(Fore.RED + "Invalid input! Please enter 1, 2, or 3." + Fore.RESET)
                print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
        except ValueError:
            print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
            print(Fore.RED + "Please enter a valid number." + Fore.RESET)
            print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    if mType == 1:
        mTypeList = "Breakfast"
    elif mType == 2:
        mTypeList = "Lunch"
    elif mType == 3:
        mTypeList = "Dinner"

    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    if mType == 1:
        print(Fore.RED + "1.", Fore.RESET + "Set-A: " + Fore.MAGENTA + "Egg and Hotdog -", Fore.BLUE + "₱50.00" + Fore.RESET)
        mPriceA = 50
        print(Fore.RED + "2.", Fore.RESET + "Set-B: " + Fore.MAGENTA + "Egg and Hungarian -", Fore.BLUE + "₱60.00" + Fore.RESET)
        mPriceB = 60
        print(Fore.RED + "3.", Fore.RESET + "Set-C: " + Fore.MAGENTA + "Egg and Ham -", Fore.BLUE + "₱70.00" + Fore.RESET)
        mPriceC = 70
    elif mType == 2:
        print(Fore.RED + "1.", Fore.RESET + "Set-A: " + Fore.MAGENTA + "Adobo -", Fore.BLUE + "₱60.00" + Fore.RESET)
        mPriceA = 60
        print(Fore.RED + "2.", Fore.RESET + "Set-B: " + Fore.MAGENTA + "Sinigang -", Fore.BLUE + "₱80.00" + Fore.RESET)
        mPriceB = 80
        print(Fore.RED + "3.", Fore.RESET + "Set-C: " + Fore.MAGENTA + "Putchero -", Fore.BLUE + "₱40.00" + Fore.RESET)
        mPriceC = 40
    elif mType == 3:
        print(Fore.RED + "1.", Fore.RESET + "Set-A: " + Fore.MAGENTA + "Paksiw -", Fore.BLUE + "₱60.00" + Fore.RESET)
        mPriceA = 60
        print(Fore.RED + "2.", Fore.RESET + "Set-B: " + Fore.MAGENTA + "Torta -", Fore.BLUE + "₱80.00" + Fore.RESET)
        mPriceB = 80
        print(Fore.RED + "3.", Fore.RESET + "Set-C: " + Fore.MAGENTA + "Nilaga -", Fore.BLUE + "₱40.00" + Fore.RESET)
        mPriceC = 40

    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    while True:
        try:
            mSet = int(input("Meal-Set: "))
            if mSet in [1, 2, 3]:
                break
            else:
                print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
                print(Fore.RED + "Invalid input! Please enter 1, 2, or 3." + Fore.RESET)
                print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
        except ValueError:
            print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)
            print(Fore.RED + "Please enter a valid number." + Fore.RESET)
            print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    numAdult = int(input("Number of Adult/s: "))
    numKid = int(input("Number of Kid's (50% Discount): "))
    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    if mSet == 1:
        mSetList = "Set-A"
        tPrice = mPriceA * (numAdult + numKid * 0.5)
    elif mSet == 2:
        mSetList = "Set-B"
        tPrice = mPriceB * (numAdult + numKid * 0.5)
    elif mSet == 3:
        mSetList = "Set-C"
        tPrice = mPriceC * (numAdult + numKid * 0.5)

    print(Back.RED + "\t CUSTOMER COPY: RECEIPT " + Back.RESET)
    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    print(f"Name: {name}")
    print(f"Meal: {mTypeList}")
    print(f"Meal Set: {mSetList}")
    print(f"Number of Adult/s: {numAdult}")
    print(f"Number of Kid/s (50% Discount): {numKid}")
    print(f"Total number of Reservation: {numKid + numAdult}")
    print(f"Total Price: ₱{tPrice}")

    print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    while True:
        payment = float(input("Payment: ₱"))
        print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

        change = payment - tPrice

        if change >= 0:
            break
        else:
            print(Fore.RED + f"Insufficient payment. You still owe " + Fore.BLUE + f"₱{-change}.")
            print(Fore.RED + "Please re-enter the payment." + Fore.RESET)
            print(Fore.YELLOW + "----------------------------------------" + Fore.RESET)

    print(Back.RED + f" Change: ₱{change} " + Back.RESET)
    print(Fore.YELLOW + "----------------------------------------\n" + Fore.RESET)

    while True:
        again = input(Fore.GREEN + "Would you like to order again? (y/n): " + Fore.RESET).lower()
        if again == 'y': 
            break
        elif again == 'n':
            print(Fore.YELLOW + "\n----------------------------------------\n" + Fore.RESET)
            print(Fore.GREEN + "Thank you for using the Program!" + Fore.RESET)
            print(Fore.YELLOW + "\n----------------------------------------\n" + Fore.RESET)
            exit()
        else:
            print(Fore.RED + "Invalid input! Please enter 'y' for yes or 'n' for no." + Fore.RESET)
