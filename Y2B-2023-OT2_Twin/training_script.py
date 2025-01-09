# Train the model locally
import os
from stable_baselines3 import PPO
import gym 
import time
from clearml import Task
from test_wrapper import OT2Env

task = Task.init(project_name="Pendulum-v1/Panagiotis", 
                 task_name="Experiment V1.1")

# Add shimmy as a requirement
Task.add_requirements("shimmy>=2.0")
os.system("pip install 'shimmy>=2.0'")

task.set_base_docker('deanis/2023y2b-rl:latest')

task.execute_remotely(queue_name="default")

env = OT2Env(render=False, max_steps=1000)

hyperparameters = {
    'n_steps': 2048,
    'batch_size': 64,
    'n_epochs': 10,
    'gamma': 0.99,
    'learning_rate': 3e-4,
    'clip_range': 0.2,
    'gae_lambda': 0.95,
    'ent_coef': 0.01,
    'vf_coef': 0.5,
    'max_grad_norm': 0.5,
}

model = PPO("MlpPolicy", env, verbose=1, **hyperparameters)

model.learn(total_timesteps=10000, progress_bar=True)