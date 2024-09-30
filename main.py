import random

print("""
----------------------------------------
-              Black Jack              -
----------------------------------------
You were given 100 chips to play with on
the house!
""")

balance = 100


def draw_card():
    random_number = random.randint(1, 13)

    if random_number == 11:
        card_number = "Jack"
        card_value = 10
    elif random_number == 12:
        card_number = "Queen"
        card_value = 10
    elif random_number == 13:
        card_number = "King"
        card_value = 10
    else:
        card_number = random_number
        card_value = random_number

    random_type = random.randint(1, 4)

    if random_type == 1:
        card_type = "Hearts"
    elif random_type == 2:
        card_type = "Clubs"
    elif random_type == 3:
        card_type = "Diamonds"
    elif random_type == 4:
        card_type = "Spades"

    return [card_value, card_number, card_type]

def display_cards(players_cards, dealers_cards):
    players_points = 0
    print("\nYour cards:")
    for card in range(0, len(players_cards)):
        print(f"{players_cards[card][1]} of {players_cards[card][2]}")
        players_points += players_cards[card][0]
    print(f"Total value: {players_points}")

    dealers_points = 0
    print("\nDealer's cards:")
    for card in range(0, len(dealers_cards)):
        print(f"{dealers_cards[card][1]} of {dealers_cards[card][2]}")
        dealers_points += dealers_cards[card][0]
    print(f"Total value: {dealers_points}")

while True:
    chips = input("To play, please enter the amount of\nchips to play with below.\nChips: ")
    
    if not chips.isdigit():
        print("\nPlease enter an integer value.")
        continue
    
    chips = int(chips)
    if chips > balance:
        print(f"\nYou only have {balance} chips.")
        continue

    print(f"\nYou bet {chips} chips.")
    
    players_cards = [draw_card(), draw_card()]
    dealers_cards = [draw_card()]
    
    display_cards(players_cards, dealers_cards)
    
    while True:
        move = input("\nYour available moves:\nh - hit\ns - stay\nChoose move: ")

        players_points = 0
        for card in players_cards:
            players_points += card[0]
        
        if move.lower() == "h":
            print("\nThe dealer dealt you a card.")
            new_card = draw_card()
            players_cards.append(new_card)
            display_cards(players_cards, dealers_cards)
            
            players_points += new_card[0]
            if players_points >= 21:
                break
        
        elif move[0].lower() == "s":
            print(f"\nYou stay your hand with {players_points} points.")
            break
        
        elif move[0].lower() not in ["h", "s"]:
            print("\nInvalid move! Try again.")
            continue
    
    dealers_points = dealers_cards[0][0]
    while dealers_points < 17:
        new_card = draw_card()
        dealers_cards.append(new_card)
        dealers_points += new_card[0]
    
    display_cards(players_cards, dealers_cards)

    if players_points > 21:
        print(f"\nYou have more than 21 points. You lost {chips} chips.")
        balance -= chips
        
    elif dealers_points > 21:
        print(f"\nDealer has more than 21 points. You win {chips * 2} chips.")
        balance += chips * 2
        
    elif dealers_points < players_points:
        print(f"\nYou win by {players_points - dealers_points} points! You receive {chips * 2} chips.")
        balance += chips * 2
        
    elif dealers_points > players_points:
        print(f"\nYou lost by {dealers_points - players_points} points. {chips} chips lost.")
        balance -= chips
        
    elif dealers_points == players_points:
        print("\nDraw.")
        
    choice = input(f"\nYou now have {balance} chips.\nWould you like to play again?\ny - yes\nn - no\nChoice: ")
    if choice.lower() == "y":
        continue
    else:
        break
