from step import *
import math
import numpy as np, random

N0 = 100
m = 2
alpha = 0
epsilon = 0
action = 0
N_state = np.zeros([40, 40])#pair of dealer and player's sum states all from -9 to 30
N_state_action = np.zeros([40, 80])#pair of dealer and player's sum states all from -9 to 30 times 2 actions
V = np.zeros([40, 80])
M = []

def monte_carlo(state, action):
    G = 0
    N_state_action[state[0] + 9, state[1] + 9 + action * 40] += 1
    N_state[state[0] + 9, state[1] + 9] += 1
    #p = random.random()
    while True:
        epsilon = N0 / (N0 + N_state[state[0] + 9, state[1] + 9])
        if random.random() <= (1 - epsilon):
            if V[state[0] + 9, state[1] + 9] > V[state[0] + 9, state[1] + 9 + 40]:
                action = 0
            else:
                action = 1
        else:
            action = random.randint(0, 1)
        state, r = step(state, action)
        N_state_action[state[0] + 9, state[1] + 9 + action * 40] += 1
        N_state[state[0] + 9, state[1] + 9] = N_state[state[0] + 9, state[1] + 9] + 1
        alpha = 1 / N_state_action[state[0] + 9, state[1] + 9 + action * 40]
        G += r
        V[state[0] + 9, state[1] + 9 + action * 40] += alpha * (G - r)
        #print(alpha)
        #if state[1] > 21 or state[1] < 1 or (action == 0 and (state[0] < 1 or state[0] >= 17)): #terminal
        if r == 1 or r == -1:
            #print(r)
            break
    return state, r

for k in range(1, 10000):
    #initialize range of both delear's first card and player's sum
    for action in range(0, 1):
        for i in range(1, 10):
            for j in range(1, 21):
                M.append(monte_carlo([i, j], action))


np.save("MC_Control.npy", M)
print ("Save Complete")