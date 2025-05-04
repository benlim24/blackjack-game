from art import logo
import random

def print_final_score (player_deck,player_score,dealer_deck,dealer_score):
    print(f"Your final hand: {player_deck}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")

def sum_deck(deck):
    while 11 in deck and sum(deck) > 21:
        deck[deck.index(11)] = 1
    return sum(deck)

while True:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game in ["y", "n"]:
        break
    else:
        print("Invalid input.")

print(logo)

while start_game == "y":
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer = [random.choice(cards),random.choice(cards)]
    player = [random.choice(cards),random.choice(cards)]
    sum_dealer = sum_deck(dealer)
    sum_player = sum_deck(player)

    if sum_player == 21 and sum_dealer == 21:
        print_final_score(player_deck=player,player_score=sum_player,dealer_deck=dealer,dealer_score=sum_dealer)
        print("You both got BlackJack! Draw :|")
    elif sum_player == 21:
        print_final_score(player_deck=player,player_score=sum_player,dealer_deck=dealer,dealer_score=sum_dealer)
        print("You got BlackJack! Congratulations! You Win! :)")
    elif sum_dealer == 21:
        print_final_score(player_deck=player,player_score=sum_player,dealer_deck=dealer,dealer_score=sum_dealer)
        print("Dealer got BlackJack! You lose :(")
    else:
        while sum_player <= 21:
            print(f"Your cards: {player}, current score: {sum_player}")
            print(f"Computer's first card: {dealer[0]}")
            take_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if take_card == 'y':
                player.append(random.choice(cards))
                sum_player = sum_deck(player)
            elif take_card == 'n':
                break
            else:
                print("Invalid input.")

        if sum_player > 21:
            print_final_score(player_deck=player,player_score=sum_player,dealer_deck=dealer,dealer_score=sum_dealer)
            print("You went over. You lose. :(")
        else:
            while sum_dealer < 16:
                dealer.append(random.choice(cards))
                sum_dealer = sum_deck(dealer)

            print_final_score(player_deck=player,player_score=sum_player,dealer_deck=dealer,dealer_score=sum_dealer)

            if sum_dealer > 21:
                print("Opponent went over. You win. :)")
            else:
                if sum_player > sum_dealer:
                    print("You Win :)")
                elif sum_player == sum_dealer:
                    print("Draw :|")
                else:
                    print("You Lose :(")

    while True:
        start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if start_game in ["y", "n"]:
            print("\n"*100)
            break
        else:
            print("Invalid input.")

print("Thank you for playing Blackjack. Goodbye!")