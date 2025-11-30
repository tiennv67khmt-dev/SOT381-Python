M = 100
r = 0.07
for nam in range (1,11):
    T = M * (1 + r)**nam
    print(f'Năm {nam}: {T:.2f} triệu')