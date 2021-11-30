import ray
from ray.rllib.agents.ppo import PPOTrainer, DEFAULT_CONFIG
import gym 
import numpy as np
from gym.spaces import Discrete, Box
import matplotlib.pyplot as plt


# Rollout Function 

def test(env, trainer=None):
    total_reward = 0

  
    state = env.reset()
    done = False
    # env.render()
    while not done:

        # This will be used when a Ray Agent is included 
        if trainer is not None:
            action = trainer.compute_single_action(state)
            state, reward, done, info = env.step(action)
            total_reward+=reward

        # This will be used to sample random actions in a environment
        else:
            action = env.action_space.sample()
            state, reward, done, info = env.step(action)
            total_reward+=reward

    print(total_reward)

