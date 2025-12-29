# B1
n = int(input("Nhập số n: "))
Tong = 0 
for i in range(0, 2*(n+1), 2):
    Tong += i
print(f"Tong = {Tong}")