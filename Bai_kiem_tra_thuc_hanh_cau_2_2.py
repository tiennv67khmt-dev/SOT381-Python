import math

n = int(input("Nhập số n: "))
S4 = 0 
for i in range(1, n+1):
    S4 += math.sqrt(3 + S4)
print(f"S4 = {S4:.5f}")