import gym
import numpy as np
from stable_baselines3 import DQN


class TradingEnv(gym.Env):
    def __init__(self, df):
        self.df = df
        self.current_step = 0
        self.done = False

    def step(self, action):
        self.current_step += 1
        reward = self.df['close'].iloc[self.current_step] * action
        return self.df.iloc[self.current_step], reward, self.done, {}

    def reset(self):
        self.current_step = 0
        return self.df.iloc[self.current_step]


env = TradingEnv(df)
model = DQN('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)