from stable_baselines3 import PPO
import gym 
import time
from clearml import Task

# Initialize ClearML task
task = Task.init(project_name="Pendulum-v1/Panagiotis", 
                 task_name="Experiment V1.0")

# Set the base Docker image
task.set_base_docker('deanis/2023y2b-rl:latest')

# Execute the task remotely
task.execute_remotely(queue_name="default")

# Log the environment creation
print("Creating the environment...")
env = gym.make('Pendulum-v1', g=9.81)
print("Environment created.")

# Log the model initialization
print("Initializing the model...")
model = PPO("MlpPolicy", env, verbose=1)
print("Model initialized.")

# Log the start of training
print("Starting training...")
model.learn(total_timesteps=10000, progress_bar=True)
print("Training completed.")