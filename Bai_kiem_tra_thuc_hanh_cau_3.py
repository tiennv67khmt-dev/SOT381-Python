n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    so = int(input(f"Nhập số thứ {i}: "))
    ds.append(so)
for j in ds:
    if j % 2 == 0 and j % 3 == 0:
        print(f"Số chia hết cho cả 2 và 3: {j}")