import random
class Agent:
    def __init__(self):
        self.Q_dictionary={}
        self.visit_count={}
        self.episode_history=[]
        self.epsilon_value=0.1
    
    def track_state(self,state_action):
        if state_action not in self.Q_dictionary:
            self.Q_dictionary[state_action]={0:0,1:0}
            self.visit_count[state_action]=1
            self.episode_history.append(state_action)
        else:
            self.visit_count[state_action]+=1
        
        
        
    #     Q = {
    # (15, 10, False): {
    #     0: 0.65,  # Stick
    #     1: 0.35   # Hit
    # },
    # (18, 6, True): {
    #     0: 0.72,
    #     1: 0.41
    # }
    # }
    
    def choose_action(self,state_action):
        random_number = random.random()
        if random_number<self.epsilon_value:
            choice =  random.choice(0,1)
            if choice:
                action =1
            else:
                action=0
        else:
            if self.Q_dictionary[state_action][0]>self.Q_dictionary[state_action][1]:
                action=0
            elif self.Q_dictionary[state_action][0]==self.Q_dictionary[state_action][1]:
                choice =  random.choice(0,1)
                if choice:
                    action =1
                else:
                    action=0
            else:
                action=1
        return action
    
    #The format we recieve on list or as in general return
    #[((15, 10, False), 1),
    # ((18, 10, False), 0)]
    def calculate_q_value(self,reward):
        #q-value for an episode considering discount factor to be 1
        for state,action in self.episode_history:
            self.Q_dictionary[state][action] = self.Q_dictionary[state][action]+(reward-self.Q_dictionary[state][action])/self.visit_count[state]
        
        
    def choose_action(self):
        return random.choice([0,1])