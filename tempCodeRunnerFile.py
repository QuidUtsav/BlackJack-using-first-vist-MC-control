for i in range(4000000):
    while env.game_status:
        state= env.get_state()
        action = agent.choose_random_action()
        agent.record_steps(state,action)
        state, reward, game_status = env.step(action)
        
    if reward==1:
            win+=1;
    elif reward==-1:
            loss+=1;
    else:
            draw+=1;
#     if (i==100000):
#             agent.epsilon_value=0   
#     agent.update_q_value(reward)
    env.reset()
#     agent.reset()
    