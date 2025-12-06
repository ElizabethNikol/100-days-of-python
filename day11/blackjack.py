import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def play_game():
    player_cards = []
    computer_cards = []
    
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    game_over = False
    
    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if player_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                player_cards.append(deal_card())
            else:
                game_over = True
    
    player_score = calculate_score(player_cards)
    
    while computer_score < 17 and player_score <= 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif player_score > computer_score:
        print("You win!")
    elif player_score == computer_score:
        print("It's a draw")
    else:
        print("You lose.")

print(art.logo)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()
    
print("Thanks for playing!")
