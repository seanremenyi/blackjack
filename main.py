import art
import random

print(art.logo)

cards = ["A","1","2","3","4","5","6","7","8","9","J","Q","K"]
suits = ["♥","♧","♢","♤"]
deck = []
for suit in suits:
    for card in cards:
        deck.append(card+suit)

def deal(amount, hand):
    for cards in range(0,amount):
        hand.append(random.choice(deck))

user_hand = []
deal(2,user_hand)
comp_hand = []
deal(2,comp_hand)

