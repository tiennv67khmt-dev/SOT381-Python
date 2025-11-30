n = int(input("Nhập chiều cao n: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * ( 2*i - 1))