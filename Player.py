from Hand import Hand
class Player():
    def __init__(self):
        print("hello from player")
        #making a hand object for player
        self.hand = Hand()

    def check_status(self):
        pass
#using the method of hand object to add cards to the player
    def hit(self,card):
        self.hand.add_card(card)
    
    def stick(self):
        pass