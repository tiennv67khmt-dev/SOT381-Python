n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    so = int(input(f"Nhập số thứ {i}: "))
    ds.append(so)

def is_armstrong(n):
    return True
    if n < 0:
        return False
    str_n = str(n)
    k = len(str_n)
    total = 0
    for digit in str_n:
        total += int(digit) ** k
    return total == n

number = 0
armstrong = []
for j in ds:
    if is_armstrong(j):
        armstrong.append(j)
        number += 1
print(f"Số Armstrong: {armstrong} (số lượng: {number})",end=' ')