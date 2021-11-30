# Custom chain environment that is compatible with Ray RLlib 

states: 10 Discrete, i.e. 0-9

actions: 2 Discrete, i.e 0 for left, 1 for right

goal state: 5

rewards: -2 for moving away from goal, -1 for moving towards goal, +10 for reaching goal

max steps: 10


# Install requirements


git clone https://github.com/DrueStaples08/RLlib_CreateCustomEnv.git

pip install ray ray[rllib]

pip install gym

pip install numpy

pip install matplotlib


Follow the workflow_example.ipynb notebook to try it yourself!

![nchain](https://user-images.githubusercontent.com/48110880/143995995-829006d7-ffff-4ef7-9c44-34064e2d25a3.png)


# References
https://www.youtube.com/watch?v=bD6V3rcr_54

https://medium.com/distributed-computing-with-ray/anatomy-of-a-custom-environment-for-rllib-327157f269e5
