# Train the model locally

from stable_baselines3 import PPO
import gym 
import time
from clearml import Task

task = Task.init(project_name="Pendulum-v1/Panagiotis", 
                 task_name="Experiment1")

task.set_base_docker('deanis/2023y2b-rl:latest')

task.execute_remotely(queue_name="default")

env = gym.make('Pendulum-v1', g=9.81)

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=10000, progress_bar=True)