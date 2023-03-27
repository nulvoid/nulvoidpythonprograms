import random
import os

# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Set up the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

# Define the function to deal a hand
def deal_hand():
    return [deck.pop(), deck.pop()]

# Define the function to calculate the value of a hand
def hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    if value > 21 and 'A' in [card[0] for card in hand]:
        value -= 10
    return value

# Define the function to display a hand
def display_hand(hand):
    for card in hand:
        print(card[0] + " of " + card[1])

# Start the game
print("Welcome to Blackjack!")
while True:
    clear_console()
    player_hand = deal_hand()
    dealer_hand = deal_hand()
    print("Your hand:")
    display_hand(player_hand)
    print("Dealer's hand:")
    print(dealer_hand[0][0] + " of " + dealer_hand[0][1])
    # Player's turn
    while hand_value(player_hand) < 21:
        action = input("Do you want to hit or stand? ")
        if action == "hit":
            player_hand.append(deck.pop())
            print("Your hand:")
            display_hand(player_hand)
            print("Dealer's hand:")
            print(dealer_hand[0][0] + " of " + dealer_hand[0][1])
        else:
            break
    player_value = hand_value(player_hand)
    if player_value > 21:
        print("Bust! You lose.")
    else:
        # Dealer's turn
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
        dealer_value = hand_value(dealer_hand)
        print("Your hand:")
        display_hand(player_hand)
        print("Dealer's hand:")
        display_hand(dealer_hand)
        if dealer_value > 21:
            print("Dealer busts! You win.")
        elif dealer_value > player_value:
            print("Dealer wins! You lose.")
        elif player_value > dealer_value:
            print("You win!")
        else:
            print("It's a tie!")
    play_again = input("Do you want to play again? ")
    if play_again.lower() != "yes":
        break
print("Thanks for playing!")
