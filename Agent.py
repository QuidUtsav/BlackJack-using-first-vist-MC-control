import random
class Agent:
    def __init__(self):
        self.Q_dictionary={}
        self.visit_count={}
        self.episode_history=[]
        self.epsilon_value=0.1
    
    #tracking only for adding new state to q value
    def track_state(self, state):
        
        if state not in self.Q_dictionary:
            self.Q_dictionary[state] = {0: 0, 1: 0}
    #record matra garna lai
    def record_steps(self,state,action):
        self.episode_history.append((state,action))
        
        
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
    
    def choose_action(self,state):

        if state not in self.Q_dictionary:
            self.track_state(state)
        random_number = random.random()
        if random_number<self.epsilon_value:
            choice =  random.choice([0,1])
            if choice:
                action =1
            else:
                action=0
        else:
            if self.Q_dictionary[state][0]>self.Q_dictionary[state][1]:
                action=0
            elif self.Q_dictionary[state][0]==self.Q_dictionary[state][1]:
                choice =  random.choice([0,1])
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
    def update_q_value(self,reward):
        visited_state= list(dict.fromkeys(self.episode_history))
            
        #q-value for an episode considering discount factor to be 1
        for state,action in visited_state:
            
            #counting the visited state within one episode
            if (state,action) not in self.visit_count:
                self.visit_count[(state,action)] = 1
            else:
                self.visit_count[(state,action)] += 1
            
            #Monte carlo control formula calculating Q(s,a) value
            self.Q_dictionary[state][action] = self.Q_dictionary[state][action]+(reward-self.Q_dictionary[state][action])/self.visit_count[(state,action)]
        
        
    # def choose_action(self):
    #     return random.choice([0,1])
    
    def reset(self):
        self.episode_history=[]
    
    def evaluation_test(self):
        self.episode_history=[]
        self.epsilon_value=0