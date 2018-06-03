from numpy import shape
from step import step
import math
import numpy as np

N0 = 100
m = 2
alpha = 0
epsilon = 0
state_array = {}
state_action_array = {}
action = 0
N_state_action = np.zeros(40, 40)
N_state = np.zeros(40, 40)

for action in range(0, 1):
    for i in range(1, 10):
        for j in range(1, 10):
            state, r = step([i, j], action);
            N_state_action[state] = N_state_action[state] + 1;
            alpha = 1 / N_state_action[state]
            epsilon = N0 / (N0 + N_state[state])




state, r = step([10, 10], action)


if state_array.has_key(state):
    state_array[state].append(state);
    N[state] = N[state] + 1



if state_array.has_key(state):
    state_array[state].append(state);
    N[state] = N[state] + 1