def laNguyenTo(n):
    kq = True
    if n == 1 or n ==2:
        kq = True
    else:
        for i in range(2, n):
            if n % i == 0: 
                kq = False
                break
    return kq