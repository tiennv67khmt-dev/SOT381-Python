n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    so = int(input(f"Nhập số thứ {i}: "))
    ds.append(so)
Tong = 0
for i in ds:
    if i % 2 == 0 or i % 3 == 0:
        Tong += i
print(f'Tổng các số chia hết cho 2 hoặc 3 là: {Tong}')