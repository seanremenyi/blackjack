import art
import random
import os

def deal():
    """returns a random card from the deck"""
    cards = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
    suits = ["♥","♧","♢","♤"]
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(card+suit)
    card = random.choice(deck)
    return card

def value(hand):
    value = 0
    ace_value = False
    for card in hand:
        if card[0] == "A":
            value += 11
            ace_value = True
        elif card[0]=="J" or card[0]=="Q" or card[0]=="K":
            value += 10
        else:
            value += int(card[0])
    if (ace_value == True) and (value > 21):
        return (value - 10)
    else:
        return value

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
      return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game():
    game_over = False
    user_hand = []
    comp_hand = []
    
    for card in range(2):
        user_hand.append(deal())
        comp_hand.append(deal())
    
    while not game_over:
        user_score = value(user_hand)
        comp_score = value(user_hand)
        
        print(f"Your card: {user_hand} and the score is {user_score}")
        print(f"The comps first card is {comp_hand[0]}")
        
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_hand.append(deal())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_hand.append(deal())
        comp_score = value(comp_hand)

    print(f"   Your final hand: {user_hand}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_hand}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("clear")
  game()
 