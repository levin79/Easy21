from numpy import random


def step(s, a): #s[1]: dealer's first card; s[2]: player's sum. a = 0: stick; a = 1: hit
    terminal = 0
    s_next = s
    r = 0

    if s[0] >= 17:
        s_next[0] = s[0]
        if a == 0:
            s_next[1] = s[1]
        else:
            p = random.random()
            if p * 3 < 2:
                s_next[1] = s[1] + random.randint(1, 10)
            else:
                s_next[1] = s[1] - random.randint(1, 10)
    else:
        s_next[1] = s[1]
        if a == 0:
            while True:
                if s[0] == 0:
                    s_next[0] = random.randint(1, 10)
                else:
                    p = random.random()
                    if p * 3 < 2: #black cards
                        s_next[0] = s[0] + random.randint(1, 10)
                    else: #red cards
                        s_next[0] = s[0] - random.randint(1, 10)
                    if s_next[0] >= 17 or s_next[0] < 1:
                        break
        else:
            p = random.random()
            if p * 3 < 2:
                s_next[1] = s[1] + random.randint(1, 10)
            else:
                s_next[1] = s[1] - random.randint(1, 10)

    if s_next[0] > s_next[1] and s_next[0] <= 21:
        r = -1
        terminal = 1
    if s_next[1] > 21 or s_next[1] < 1:
        r = -1
        terminal = 1
        
    if s_next[0] == s_next[1] and a == 0 and s_next[0] >= 17:
        r = 0
        terminal = 1

    if s_next[0] < s_next[1] and s_next[1] <= 21 and s_next[0] >= 17:
        r = 1
        terminal = 1
    if s_next[0] > 21 or s_next[0] < 1:
        r = 1
        terminal = 1
        
    return s_next, r, terminal