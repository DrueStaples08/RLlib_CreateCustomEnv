import ray
from ray.rllib.agents.ppo import PPOTrainer, DEFAULT_CONFIG
import gym 
import numpy as np
from gym.spaces import Discrete, Box
import matplotlib.pyplot as plt



# Ray Environment
class InnerChainEnv(gym.Env):
    # Use env_config as a parameter so it's compatible with Ray
    def __init__(self, env_config=None):
        env_config = {}

        # Action space 
        self.action_space = Discrete(2)

        # Observation space
        self.observation_space = Discrete(10)

        # Start states - do NOT include terminal state
        self.state = np.random.choice([i for i in range(self.observation_space.n) if i != 5])

        # Time length or max steps
        self.length = 9

        # Seed the values so the same results are reproduceable 
        self.seed(42)
        
        # Reset the the environment everytime a new object is instantiated from this parent class
        self.reset()


    def reset(self):
        # Instatiate the state, reward, done, info, and length to it's initial value
        self.state  = np.random.choice([i for i in range(self.observation_space.n) if i != 5])
        self.reward = 0
        self.done = 0
        self.info = {}
        self.length = 9

        return self.state    



    def step(self, action):
        # It's good practice to ensure your action e.g. 0 and 1 is included in the action space 
        assert self.action_space.contains(action)   

        # Reward and state systems for our agent taking a single action
        # 5 is our goal state (0-9)
        # We receive a reward of 10 when we reach our goal
        # We have two actions: move left (0) or move right (1)
        # If we move towards the goal, we receive a reward of -1
        # If we move away from the goal, we receive a reward of -2 
        if self.state == 5:
            self.reward = 10
            self.done = 1

        # Steps for our agent. The max steps for our agent is 10, 
        # so the episode ends on the tenth timestep
        elif self.length <= 0:
            self.done = 1
            
        else:
            assert self.action_space.contains(action)
            self.length-= 1

            if action == 0:
                if self.state == 0:
                    self.reward = -2
                elif self.state < 5:
                    self.reward = -2
                    self.state-=1
                else:
                    self.state-=1
                    if self.state == 5:
                        self.reward = 10
                        self.done = 1
                    else:
                        self.reward = -1
        
            else:
                if self.state == 9:
                    self.reward = -2
                elif self.state > 5:
                    self.reward = -2
                    self.state+=1
                else:
                    self.state+=1
                    if self.state == 5:
                        self.reward = 10
                        self.done = 1
                    else:
                        self.reward = -1

        return self.state, self.reward, self.done, self.info


    def render(self):
        pass
        # This is where a simulation can be created 
        # to replicate the agent and environment e.g. Pygame

    
