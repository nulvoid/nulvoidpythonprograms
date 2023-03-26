import random

# Set up initial variables
money = 100
chocolate_bars = 0
sugar = 0
cocoa = 0
milk = 0

# Welcome message
print("Welcome to the Chocolate Making Game!")
print("You have $100 to start with.")
print("You need to buy ingredients to make chocolate bars and sell them to the highest bidder.")
print("Good luck!")

# Function for buying ingredients
def buy_ingredient(ingredient, cost):
    global money, sugar, cocoa, milk
    amount = int(input(f"How many {ingredient}s would you like to buy? "))
    total_cost = amount * cost
    if money >= total_cost:
        money -= total_cost
        if ingredient == "sugar":
            sugar += amount
        elif ingredient == "cocoa":
            cocoa += amount
        elif ingredient == "milk":
            milk += amount
        print(f"You bought {amount} {ingredient}s.")
    else:
        print("You don't have enough money to buy that many ingredients.")

# Function for selling chocolate bars
def sell_chocolate():
    global money, chocolate_bars
    if chocolate_bars > 0:
        price = random.randint(5, 15)
        money += price
        chocolate_bars -= 1
        print(f"You sold a chocolate bar for ${price}.")
    else:
        print("You don't have any chocolate bars to sell.")
        
# Game loop
while True:
    # Show the player's current status
    print(f"You have ${money}.")
    print(f"You have {sugar} sugar, {cocoa} cocoa, and {milk} milk.")
    print(f"You have {chocolate_bars} chocolate bars.")

    # Ask the player what they want to do
    choice = input("What would you like to do? (buy/sell/make/quit) ").lower()

    # Buy ingredients
    if choice == "buy":
        ingredient_choice = input("What ingredient would you like to buy? (sugar/cocoa/milk) ").lower()
        if ingredient_choice == "sugar":
            buy_ingredient("sugar", 2)
        elif ingredient_choice == "cocoa":
            buy_ingredient("cocoa", 3)
        elif ingredient_choice == "milk":
            buy_ingredient("milk", 5)
        else:
            print("Sorry, that's not a valid choice.")

    # Sell chocolate bars
    elif choice == "sell":
        sell_chocolate()

    # Make chocolate bars
    elif choice == "make":
        if sugar >= 2 and cocoa >= 1 and milk >= 1:
            sugar -= 2
            cocoa -= 1
            milk -= 1
            chocolate_bars += 1
            print("You made a chocolate bar!")
        else:
            print("You don't have enough ingredients to make a chocolate bar.")

    # Quit the game
    elif choice == "quit":
        print("Thanks for playing!")
        break

    # Invalid choice
    else:
        print("Sorry, that's not a valid choice.")
