from Player import Player
from Dealer import Dealer
from Deck import Deck
class Environment():
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.game_status = True
        self.deck = Deck()
        self.player_win=False
        self.dealer_win=False
        self.reward=0
        self.first_play()
        
        
    #reseting environment for reaching terminal state
    def reset(self):
        self.player= Player()
        self.dealer =Dealer()
        self.reward=0
        self.game_status=True
        self.player_win=False
        self.dealer_win=False
        self.first_play()
        
        return self.get_state()
    
    
    def first_play(self):    
        for _ in range(2):
            self.player.hit(self.deck.pick_card())
            self.dealer.hit(self.deck.pick_card())

        
    def get_state(self):
        return (self.player.hand.calculate_total(),
            self.dealer.hand.cards[0],
            self.player.hand.usable_ace)
    
    def step(self,action):
        if not self.game_status:
            return self.get_state(),self.reward,self.game_status
        if action==1: #Hit 3, 14, 18
            self.player.hit(self.deck.pick_card())
            
            if self.player.hand.detect_bust():
                #If the player busts we flag it calculate the reward and terminate the game
                self.dealer_win=True
                self.reward=self.calculate_reward()
                self.game_status=False
                return self.get_state(),self.reward,self.game_status
            self.reward=self.calculate_reward()
            
        elif action==0: #Stick  4 8 14
            while self.dealer.should_hit():
                self.dealer.hit(self.deck.pick_card())
                
                #NOw the dealer hits till the condition 
                if self.dealer.hand.detect_bust():
                #If the dealer busts we flag it calculate the reward and terminate the game
                    self.player_win=True
                    self.reward=self.calculate_reward()
                    self.game_status=False
                    return self.get_state(),self.reward,self.game_status
                
                    #Given that condition breached we end the game as the environment
            self.game_status= False
        self.reward = self.calculate_reward()
        return self.get_state(),self.reward,self.game_status
    
    
    def calculate_reward(self):
        if self.player_win:
            return 1;
        if self.dealer_win:
            return -1;
        if not self.game_status:
            if (self.player.hand.calculate_total()>self.dealer.hand.calculate_total()):
                return 1;
            elif self.player.hand.calculate_total()<self.dealer.hand.calculate_total():
                return -1;
            else:
                return 0;
        else:
            return 0;
