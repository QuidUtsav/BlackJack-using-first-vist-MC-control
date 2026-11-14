# This file contains the baseline for first visit monte carlo control
# I will be using epsilon-greedy for exploration 
# In monte carlo we basically evaluate through complete episodes
# and improve the policy through our observed returns.
import random
import math
class Environment:
    
    def __init__(self):
        print("i have been pickled")
        self.player_sum=0
        self.dealer_first_card=0
        self.usable_ace=False
        self.game_status=True
        
    def show_state(self):
        print(self.player_sum,self.dealer_first_card,self.usable_ace)
        
    def hit(self,player):
        Hand.hit(player)
        if(Player.total_sum>20):
            self.game_status=False
        
        
class Player:
    def __init__(self):
        self.total_sum=0
        
    def hit(self):
        pass
        

class Dealer:
    pass

class Deck:
    def __init__(self):
        pass
    
    def generate_card():
        card = math.floor(random.random()*10+1)
        return
        
        
    pass

class Hand:
    def __init__(self):
        self.new_card=0

    def hit(self,player):
        new_card = Deck.generate_card()
        if new_card==1:
            player.usable_ace=True
        player.total_sum+=new_card
            
            
a = Environment()
a.show_state()