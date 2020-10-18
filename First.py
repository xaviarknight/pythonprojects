#Logic: Card class - Understand suit of class
#understand Rank
# Correspond to tha rank there should be an integer value

#create Deck class

# Player class- ti hold card

#Creating card classs

import random
suits = ('Hearts','Diamonds','Spades','Club')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value= values[rank]

    def __str__(self):
        return self.rank +"of"+self.suit
 
 #Deck class: We will see that deck class holds a lict of card objects

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)

#Player class is to hold cards by a player
# Draw a card from top
# Add a card in deck from bottom 
# we will assume this process
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player{self.name} has {len(self.all_cards)} cards.'
#Game Logic Begins from here--Toughest Part
#Game setup 
#while loops game_one
    #while at_war

player_one = Player("One")
player_two= Player("Two")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num +=1
    print(f"Round {round_num}")
    if len(player_one.all_cards)==0:
        print('Player One, Out of cards! Player One wins')
        game_on = False
        break
    if len(player_two.all_cards)==0:
        print('Player Two, Out of cards! Player Two wins')
        game_on = False
        break

    # Start a new round
    player_one_cards =[]
    player_one_cards.append(player_one_cards.remove())
    player_two_cards =[]
    player_two_cards.append(player_two_cards.remove())

    #WHILE AT WAR
    #EACH PLAYER HAS TO TAKE FIVE CARDS
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_twp.add_cards(player_two_cards)
            at_war=False
        else:
            print('War!')

            if len(player_one.all_cards) < 3:
                print("Player one is unable to declare war")
                print('Player two wins')
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player two is unable to declare war")
                print('Player one wins')
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


