# This file contains the baseline for first visit monte carlo control
# I will be using epsilon-greedy for exploration 
# In monte carlo we basically evaluate through complete episodes
# and improve the policy through our observed returns.
from Environment import Environment
import random
env = Environment()

for episode in range(5):
    state = env.reset()

    while env.game_status:
        action = random.choice([0, 1])
        next_state, reward, done = env.step(action)

    print(f"Episode {episode + 1}: Reward = {reward}")