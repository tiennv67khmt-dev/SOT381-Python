n = int(input("Nhập n (0<n<10): "))
giai_thua = 1
while n <= 0 or n >= 10:
    n = int(input("Nhập lại n (0<n<10): "))
for i in range(1, n + 1):
    giai_thua *= i
print(f"{n}! = {giai_thua}")