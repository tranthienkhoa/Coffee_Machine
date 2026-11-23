class CoffeeMachine:
    def __init__(
        self, cash=550, machine_water=400, machine_milk=540, machine_beans=120, cups=9
    ):
        self.cash = cash
        self.machine_water = machine_water
        self.machine_milk = machine_milk
        self.machine_beans = machine_beans
        self.cups = cups
        self.state = "choosing action"
        print("Write action (buy, fill, take, remaining, exit):")

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.machine_water} ml of water")
        print(f"{self.machine_milk} ml of milk")
        print(f"{self.machine_beans} grams of coffee beans")
        print(f"{self.cups} disposable cups")
        print(f"${self.cash} of money\n")

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        if self.machine_water < water_needed:
            print("Sorry, not enough water!\n")
        elif self.machine_milk < milk_needed:
            print("Sorry, not enough milk!\n")
        elif self.machine_beans < beans_needed:
            print("Sorry, not enough coffee beans!\n")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!\n")
        else:
            print("I have enough resources, making you a coffee!\n")
            self.machine_water -= water_needed
            self.machine_milk -= milk_needed
            self.machine_beans -= beans_needed
            self.cups -= 1
            self.cash += cost

    def handle_input(self, user_input):
        if self.state == "choosing action":
            if user_input == "buy":
                self.state = "choosing coffee"
                print(
                    "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
                )
            elif user_input == "fill":
                self.state = "filling water"
                print("\nWrite how many ml of water you want to add:")
            elif user_input == "take":
                print(f"\nI give you ${self.cash}\n")
                self.cash = 0
                print("Write action (buy, fill, take, remaining, exit):")
            elif user_input == "remaining":
                self.print_state()
                print("Write action (buy, fill, take, remaining, exit):")

        elif self.state == "choosing coffee":
            if user_input == "1":
                self.make_coffee(250, 0, 16, 4)
            elif user_input == "2":
                self.make_coffee(350, 75, 20, 7)
            elif user_input == "3":
                self.make_coffee(200, 100, 12, 6)
            self.state = "choosing action"
            print("Write action (buy, fill, take, remaining, exit):")

        elif self.state == "filling water":
            self.machine_water += int(user_input)
            self.state = "filling milk"
            print("Write how many ml of milk you want to add:")

        elif self.state == "filling milk":
            self.machine_milk += int(user_input)
            self.state = "filling beans"
            print("Write how many grams of coffee beans you want to add:")

        elif self.state == "filling beans":
            self.machine_beans += int(user_input)
            self.state = "filling cups"
            print("Write how many disposable cups you want to add:")

        elif self.state == "filling cups":
            self.cups += int(user_input)
            self.state = "choosing action"
            print("\nWrite action (buy, fill, take, remaining, exit):")


if __name__ == "__main__":
    machine = CoffeeMachine()
    while True:
        action = input()
        if action == "exit":
            break
        machine.handle_input(action)
