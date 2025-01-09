# Task 9 - Simulation Project

## Overview
This project contains a simulation of an agent within a defined space. The simulation is initialized with a specific
set of defined corners in which the robot is tasked to follow. It's interactions are observed and are listed within this README markdown file.

## Project Structure
- `task_9.py`: Main script to run the simulation.
- `sim_class.py`: Contains the `Simulation` class and related methods.
- `README.md`: Project documentation.

## Requirements
- Python 3.x
- Anaconda (recommended for managing dependencies)
- Pybullet

## Setup
1. Install ByBullet:
    ```sh  
    conda install -c conda-forge pybullet
    ```

2. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```
    
3. Create and activate the conda environment:
    ```sh
    conda create --name block2b_gpu python=3.x
    conda activate block2b_gpu
    ```

## Running the Simulation
1. Activate the Conda Environment:
    ```sh  
    conda activate block2b_gpu
    ```

2. Navigate to the project directory:
    ```sh
    cd "C:\Users\panay\Desktop\BUAS\YEAR 2\REPOSITORIES\2024-25b-fai2-adsai-PanayiotisEvangelou233096\tasks\TASK 9\Y2B-2023-OT2_Twin"
    ```

3. Run the simulation script:
    ```sh
    python task_9.py
    ```

## Working Envelope of the Pipette

The working envelope of the pipette is defined by the following corners:
- Corner 1: [-1, 1, 1, 0]
- Corner 2: [1, -1, 1, 0]
- Corner 3: [-1, -1, 1, 0]
- Corner 4: [1, 1, 1, 0]
- Corner 5: [-1, 1, -1, 0]
- Corner 6: [1, -1, -1, 0]
- Corner 7: [-1, -1, -1, 0]
- Corner 8: [1, 1, -1, 0]

## Expected output

- Corner 1 final position: [-0.26001621250424495, 0.13000812646777501, 0.20000197612124115]
- Corner 2 final position: [0.18023397915753858, -0.2600019984480169, 0.1999992742155521]
- Corner 3 final position: [-0.2601187923680583, -0.260002364370992, 0.19999878187011064]
- Corner 4 final position: [0.18023361936488794, 0.13000860842337772, 0.20000242333611537]
- Corner 5 final position: [-0.26000155447694473, 0.13022961912733358, 0.07895207051962469]
- Corner 6 final position: [0.1800929877237951, -0.26000157112327044, 0.079888362290187]
- Corner 7 final position: [-0.2600034195147701, -0.26002070416967654, 0.07988743463480572]
- Corner 8 final position: [0.18000006320498665, 0.13001445860706595, 0.0799118792853605]


