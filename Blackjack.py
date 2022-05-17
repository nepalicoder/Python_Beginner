import random


def deal_cards():
    """ return random cards from a deck"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # generate random cards for player anbd computer
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return " Computer has a Blackjack, computer wins"
    elif user_score == 0:
        return " Player has a Blackjack, Player wins "
    elif user_score > 21:
        return " You went over and compter wins"
    elif computer_score > 21:
        return " Computer went over and you win"
    elif user_score > computer_score:
        return "User wins"
    else:
        return "You win"


user_card = []
computer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_cards())
    computer_card.append(deal_cards())

while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"your cards{user_card} and your score {user_score}")
    print(f"computer card is {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        player_wants_to_play = input("Do you want to pick another card? pick 'y' for yes and 'n' for no: ")
        if player_wants_to_play == "y":
            user_card.append(deal_cards())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_cards())
    computer_score = calculate_score(computer_card)

print(f" \nYour final hand is {user_card} and final score is {user_score}")
print(f" Computer's final hand is {computer_card} and final score is {computer_score}")
print(compare(user_score, computer_score))