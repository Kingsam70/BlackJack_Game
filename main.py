from logo import logo
import random

# The cards are not removed from the deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# cards = [11, 11, 11, 11, 1]


def get_random_card():
    """returns a random card from the deck of cards"""
    return random.choice(cards)


user_cards = []
computer_cards = []

# # Below code up to the function--> check_winner() is for giving initial cards to the user and to computer

# Below code to ensure that no two 11's were drawn from the deck of cards as the sum of the first two cards are always less than 21.
while len(user_cards) < 2:
    user_cards.append(get_random_card())
    if sum(user_cards) > 21:
        user_cards = []  # resetting user_cards if the sum is more than 21

# Appending the very first card to the list of computer's card
computer_cards.append(get_random_card())


def check_winner():
    if sum(user_cards) > 21:
        return "You went over. You loose 😤"
    elif sum(computer_cards) > 21:
        return "Computer went over. You win 😊"
    elif sum(user_cards) > sum(computer_cards):
        return "You win 😊"
    elif sum(computer_cards) > sum(user_cards):
        return "You loose 😤"
    else:
        return "Draw👌"


def game():
    """The main core of the game implements the basic logic asks for user input and checks winner using the above function """
    print(logo)
    print(f"    Your Cards: {user_cards}, current score {sum(user_cards)}.")
    print(f"    Computer's first card: {computer_cards[0]}")
    if sum(user_cards) == 21:  # here len(user_card) is 2
        print("\nWin with a BlackJack 😜")
        return

    while True:
        user_input = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
        if user_input == "y":
            user_cards.append(get_random_card())
            print(f"\n    Your Cards: {user_cards}, current score {sum(user_cards)}.")
            print(f"    Computer's first card: {computer_cards[0]}")

            if "loose" in check_winner():
                print("\nYou loose 😒")
                return

        elif user_input == "n":
            while sum(computer_cards) < 17:  # Appending a random card in computer's card until it becomes more than 17
                computer_cards.append(get_random_card())
            print(f"\nYour final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n")

            print(check_winner())
            break


game()
