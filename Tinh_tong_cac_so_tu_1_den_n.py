n = int(input('nhập vào một số nguyên: '))
tong = 0
for i in range(1, n + 1):
    tong += i
print(f'tổng các số từ 1 đến {n} là: {tong}')