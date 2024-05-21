
#Serie di leibinz
def leibinz(max=10000) -> float:    
    inner = 1 
    for i in range(1, max): 
        if i % 2 == 0: 
            inner += 1 / (2 * i + 1)
        else: 
            inner -= 1 / (2 * i + 1)
    return inner * 4 

#Serie di Nilakantha
def nilakantha(max=10000) -> float:
    inner = 0
    add = True
    for i in range(2, max, 2):
        if add:
            inner += 1 / (i * (i + 1) * (i + 2))
        else: 
            inner -= 1 / (i * (i + 1) * (i + 2))
        add = not add
    return 3 + 4 * (inner)

#Formula di Machin
def machin() -> float: 
    from math import atan
    pi = 4 * (4 * atan(1/5) - atan(1/239))
    return pi

#Montecarlo
def montecarlo(max=1000) -> float: 
    from random import uniform
    inside_circle = 0 
    for _ in range(max): 
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1: 
            inside_circle += 1
        
    return (inside_circle / max) * 4