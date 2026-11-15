from Hand import Hand
class Dealer():
    def __init__(self):
        # print("hello from Dealer")
        self.hand=Hand()

    def hit(self,card):
        self.hand.add_card(card)
    
    def should_hit(self):
        #we set a rule for dealer to only play if he has card value below 17
        return self.hand.calculate_total() <17