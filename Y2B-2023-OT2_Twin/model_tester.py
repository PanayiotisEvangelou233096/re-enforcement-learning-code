from stable_baselines3 import PPO
import gym 
import time
from test_wrapper import OT2Env

env = OT2Env(should_render=False, max_steps=1000)

model = PPO.load("ppo_model.zip")

obs = env.reset()
total_reward = 0
for step in range(1000):  # Run for 1000 steps or until the episode ends
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env.step(action)
    total_reward += reward
    env.render()
    if done or truncated:
        print(f"Episode finished after {step + 1} steps with total reward: {total_reward}")
        obs = env.reset()
        total_reward = 0  # Reset total reward for the next episode
    else:
        print(f"Step {step + 1}: reward={reward}, total_reward={total_reward}")

print("Testing completed.")