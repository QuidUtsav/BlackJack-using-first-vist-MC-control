class Hand:
    def __init__(self):
        self.total_card_value=0
        self.usable_ace=False
        
    def add_card(self,card_value):
        self.total_card_value+=card_value
        
        
    def calculate_total(self):
        if self.usable_ace and self.total_card_value<10:
# so ma sanga ace xa ani ace lai sum garera mero value 10 vanda kaam xa vane ace ko value 11 set garni
            self.total_card_value+=10
            return self.total_card_value
        else:
            return self.total_card_value
            
    def detech_bust(self):
        if self.total_card_value>21:
            print("You go busted!!!")