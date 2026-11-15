class Hand:
    def __init__(self):
        self.total_card_value=0
        self.usable_ace=False
        self.cards=[]
        
    def add_card(self,card):
        self.cards.append(card)

    
    def calculate_total(self):
        self.usable_ace = 1 in self.cards
        self.total_card_value = sum(self.cards)
        if self.usable_ace and self.total_card_value+10<21:
# so ma sanga ace xa ani ace lai sum garera mero value 10 vanda kaam xa vane ace ko value 11 set garni
            self.total_card_value+=10

            return self.total_card_value
        else:
            return self.total_card_value
            
    def detect_bust(self):
        self.total_card_value = sum(self.cards)
        if self.total_card_value>21:
            return True
        else:
            return False
        
    def usable_ace(self):
        self.total_card_value = sum(self.cards)
        return 1 in self.cards and self.total_card_value+10<21