def giai_thua(n):
    kq = 1
    for i in range(1, n+1):
        kq = kq * i
    return kq
print(giai_thua(5))