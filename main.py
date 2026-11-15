# This file contains the baseline for first visit monte carlo control
# I will be using epsilon-greedy for exploration 
# In monte carlo we basically evaluate through complete episodes
# and improve the policy through our observed returns.
from Environment import Environment
from Agent import Agent

env = Environment()
Agent = Agent()
env.reset()
win=0
loss=0
draw=0
for _ in range(1000):
    while env.game_status:
        action = Agent.choose_action()
        observation, reward, game_status = env.step(action)
    if reward==1:
            win+=1;
    elif reward==-1:
            loss+=1;
    else:
            draw+=1;
    env.reset()
print(f"Wins={win},\nlosses={loss}\ndraws={draw}")