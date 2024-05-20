
#Serie di leibinz -> FUNZIONA
def leibinz(max=10000) -> float:    
    inner = 1 
    for i in range(1, max): 
        if i % 2 == 0: 
            inner += 1 / (2 * i + 1)
        else: 
            inner -= 1 / (2 * i + 1)
    return inner * 4 