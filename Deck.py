import random
import math
class Deck:
    def __init__(self):
        pass
    
    def pick_card(self):
        num = random.random()
        card = math.floor(num/(4/52))+1
        card = card if card<10 else 10
        return card