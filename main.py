# This file contains the baseline for first visit monte carlo control
# I will be using epsilon-greedy for exploration 
# In monte carlo we basically evaluate through complete episodes
# and improve the policy through our observed returns.
from Environment import Environment
from Agent import Agent

env = Environment()
agent = Agent()
env.reset()
win=0
loss=0
draw=0
for i in range(1000000):
    while env.game_status:
        state= env.get_state()
        action = agent.choose_action(state)
        agent.record_steps(state,action)
        state, reward, game_status = env.step(action)
        
    if reward==1:
            win+=1;
    elif reward==-1:
            loss+=1;
    else:
            draw+=1; 
    agent.update_q_value(reward)
    env.reset()
    agent.reset()
    
    
    
# Evaluation PART
agent.epsilon_value = 0

eval_win = 0
eval_loss = 0
eval_draw = 0

for i in range(100000):

    while env.game_status:
        state = env.get_state()
        action = agent.choose_action(state)

        state, reward, game_status = env.step(action)

    if reward == 1:
        eval_win += 1
    elif reward == -1:
        eval_loss += 1
    else:
        eval_draw += 1

    env.reset()
print("TRAINING SECTION")
print(f"Wins={win},\nlosses={loss}\ndraws={draw}\n")#helo helo
print("\n===============================================================================\n")
print("\n--- Evaluation Results ---")
print(f"Wins: {eval_win}")
print(f"Losses: {eval_loss}")
print(f"Draws: {eval_draw}")
print(f"Average Reward: {(eval_win - eval_loss) / 100000:.5f}")
    
    
    
    
    
    
    
    
    
    #DECAYING EPSILON
# for i in range(4000000):

#     agent.decay_epsilon(i)

#     while env.game_status:
#         state = env.get_state()
#         action = agent.choose_action(state)

#         agent.record_steps(state, action)

#         state, reward, game_status = env.step(action)
#     if reward==1:
#             win+=1;
#     elif reward==-1:
#             loss+=1;
#     else:
#             draw+=1;     
#     agent.update_q_value(reward)

#     env.reset()
#     agent.reset()
    
