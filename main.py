import random
from replit import clear
from art import logo
print(logo)

def deal_card():
    """"Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Remíza!"
    elif computer_score == 0:
        return "Dealer má BlackJack, PROHRÁVÁTE!"
    elif user_score == 0:
        return "Máte BlackJack, VYHRÁVÁTE!"
    elif user_score > 21:
        return "Máte přes 21, PROHRÁVÁTE!"
    elif computer_score > 21:
        return "Dealer má přes 21, VYHRÁVÁTE!"
    elif user_score > computer_score:
        return "Máte víc, VYHRÁVÁTE!"
    else:
        return "Dealer má víc, PROHRÁVÁTE!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Vaše karty: {user_cards}, hodnota: {user_score}")
        print(f"   Dealerova první karta: {computer_cards[0]}")
            
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("'A' pro další kartu, 'N' pro hru dealera: ")
            if user_should_deal == "A" or "a":
                user_cards.append(deal_card())
            if user_should_deal == "N" or "n":
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print("*" * 20)
    print(f"  Vaše finální karty: {user_cards}, hodnota: {user_score}")
    print(f"  Dealerovy finální karty: {computer_cards}, hodnota: {computer_score}")
    print(compare(user_score, computer_score))
    print("*" * 20)
     
while input("NOVÁ HRA? \n zadejte 'A' = ANO\n zadejte 'N' = NE\n ") == "A" or "a":
    clear()
    play_game()
