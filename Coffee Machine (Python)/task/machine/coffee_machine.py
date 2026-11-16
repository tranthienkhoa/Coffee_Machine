cash = 550
machine_water = 400
machine_milk = 540
machine_beans = 120
cups = 9


def print_state():
    print("\nThe coffee machine has:")
    print(f"{machine_water} ml of water")
    print(f"{machine_milk} ml of milk")
    print(f"{machine_beans} grams of coffee beans")
    print(f"{cups} disposable cups")
    print(f"${cash} of money\n")


def make_coffee(water_needed, milk_needed, beans_needed, cost):
    global machine_water, machine_milk, machine_beans, cups, cash

    if machine_water < water_needed:
        print("Sorry, not enough water!\n")
    elif machine_milk < milk_needed:
        print("Sorry, not enough milk!\n")
    elif machine_beans < beans_needed:
        print("Sorry, not enough coffee beans!\n")
    elif cups < 1:
        print("Sorry, not enough disposable cups!\n")
    else:
        print("I have enough resources, making you a coffee!\n")
        machine_water -= water_needed
        machine_milk -= milk_needed
        machine_beans -= beans_needed
        cups -= 1
        cash += cost


while True:
    user_input = input("Write action (buy, fill, take, remaining, exit):\n")

    if user_input == "buy":
        user_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if user_buy == "1":
            make_coffee(250, 0, 16, 4)
        elif user_buy == "2":
            make_coffee(350, 75, 20, 7)
        elif user_buy == "3":
            make_coffee(200, 100, 12, 6)
        elif user_buy == "back":
            continue

    elif user_input == "fill":
        machine_water += int(input("Write how many ml of water you want to add:\n"))
        machine_milk += int(input("Write how many ml of milk you want to add:\n"))
        machine_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        cups += int(input("Write how many disposable cups you want to add:\n"))

    elif user_input == "take":
        print(f"I give you ${cash}\n")
        cash = 0

    elif user_input == "remaining":
        print_state()

    elif user_input == "exit":
        break