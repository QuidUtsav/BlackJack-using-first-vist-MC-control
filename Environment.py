from Player import Player
from Dealer import Dealer
from Deck import Deck
class Environment():
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.game_status = True
        self.deck = Deck()
        self.first_play()
    #reseting environment for reaching terminal state
    def reset(self):
        self.player= Player()
        self.dealer =Dealer()
        self.game_status=True
        self.first_play()
    def first_play(self):    
        for _ in range(2):
            self.player.hit(self.deck.pick_card())
            self.dealer.hit(self.deck.pick_card())
        print(self.get_state())
        
    def get_state(self):
        return (
            self.player.hand.calculate_total(),
            self.dealer.hand.cards[0],
            self.player.hand.usable_ace
        )
    
    def step(self,action):
        if action==1: #Hit
            self.player.hit(self.deck.pick_card())
            
            if self.player.hand.detect_bust():
                self.game_status=False
        
        elif action==0: #Stick
            while self.dealer.should_hit():
                self.dealer.hit(self.deck.pick_card())
            
            self.game_status=False
        
        return self.get_state()
    
