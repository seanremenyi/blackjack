import art
import random
import os

cards = ["A","1","2","3","4","5","6","7","8","9","J","Q","K"]
suits = ["♥","♧","♢","♤"]

def new_deck():
    for suit in suits:
        deck = []
        for card in cards:
            deck.append(card+suit)
        return deck

def deal(amount, hand, deck):
    for cards in range(0,amount):
        hand.append(random.choice(deck))

def value(hand):
    value = 0
    ace_value = False
    for card in hand:
        if card[0] == "A":
            value += 1
            ace_value = True
        elif card[0]=="J" or card[0]=="Q" or card[0]=="K":
            value += 10
        else:
            value += int(card[0])
    if ace_value == False:
        return value
    else:
        return f"{value} or {value + 10}"

print(art.logo)        
deck = new_deck()
user_hand = []
deal(2,user_hand,deck)
comp_hand = []
deal(2,comp_hand,deck)

print(user_hand)
print(value(user_hand))

