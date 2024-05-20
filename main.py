
#Serie di leibinz 
def leibinz(max=1000) -> float:     
    inner = 1
    for i in range(1, max, 1): 
            term = 1 / (2 * i + 1)
            if i % 2 == 0: 
                inner += term
            else: 
                inner -= term
    return 4 * inner
print(leibinz())