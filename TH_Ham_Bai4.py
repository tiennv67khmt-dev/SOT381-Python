def CtoF(doC):
    doF  = (9/5) * doC + 32
    return doF
doC = 37
doF = CtoF(doC)
print(f'{doC} độ C = {doF:.2f} độ F')