import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S = math.sqrt(x + S)
print(f"S = {S:.2f}")

S2 = 0
for i in range(2, n):
    S2 += x**i/i+1
print(f'S2 = {S2:.2f}')