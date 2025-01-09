import os
from stable_baselines3 import PPO
from clearml import Task
from test_wrapper import OT2Env

# Initialize ClearML Task
Task.add_requirements("shimmy>=2.0")
os.system("pip install shimmy>=2.0")

task = Task.init(
    project_name="Mentor Group K/Group 2",
    task_name="shitfuck 2"
)

task.set_base_docker('deanis/2023y2b-rl:latest')
task.execute_remotely(queue_name="default")

# Initialize Environment
print("Creating OT2 environment...")
env = OT2Env(render=False, max_steps=1000)

# Define Hyperparameters
hyperparameters = {
    'n_steps': 1024,
    'batch_size': 32,
    'n_epochs': 4,
    'gamma': 0.99,
    'learning_rate': 1e-4,
    'clip_range': 0.2,
    'gae_lambda': 0.95,
    'ent_coef': 0.01,
    'vf_coef': 0.5,
    'max_grad_norm': 0.5,
}

# Initialize and Train Model
model = PPO("MlpPolicy", env, verbose=1, **hyperparameters)
print("Starting training...")
model.learn(total_timesteps=10000, progress_bar=True)
print("Training completed.")

# Save the model
model_path = "ppo_model.zip"
model.save(model_path)

# Upload model
task.upload_artifact(name="trained_model", artifact_object=model_path)
