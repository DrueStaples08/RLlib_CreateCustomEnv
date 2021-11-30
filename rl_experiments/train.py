from ray.rllib.agents.ppo import PPOTrainer, DEFAULT_CONFIG
import gym 
import numpy as np
from gym.spaces import Discrete, Box
import matplotlib.pyplot as plt


def train(trainer, episodes=10, all_results=False):
        # Our most import metrics include rewards and length

    episode_reward_max = []
    episode_reward_min = []
    episode_reward_mean = []
    episode_length_mean = []

    for i in range(episodes):
        result = trainer.train()
        if all_results:
            print(result)
        else:
            episode_reward_max.append(result['episode_reward_max'])
            episode_reward_min.append(result['episode_reward_min'])
            episode_reward_mean.append(result['episode_reward_mean'])
            episode_length_mean.append(result['episode_len_mean'])
    trainer.save()
    print('Agent Saved')
    return episode_reward_max, episode_reward_min, episode_reward_mean, episode_length_mean 