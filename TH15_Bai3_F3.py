n = int(input("Nhập N: "))
tong = 0
for i in range(1, n + 1):
    tong += i
    if tong % 2 == 0 and tong % 3 == 0:
        print(tong)