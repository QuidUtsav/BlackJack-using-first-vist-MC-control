# This file contains the baseline for first visit monte carlo control
# I will be using epsilon-greedy for exploration 
# In monte carlo we basically evaluate through complete episodes
# and improve the policy through our observed returns.
from Environment import Environment

play = Environment()

while True:
    while play.game_status:
        act = int(input("1 or 0:\n"))
        print(play.step(act))
    play.result()
    play.reset()