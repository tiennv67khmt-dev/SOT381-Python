print('nhập a: ',end='')
a = float(input())
print('nhập b: ',end='')
b = float(input())
if a == 0:
    if b == 0:
        print('Phương trình có vô số nghiệm')
    elif b != 0:
        print('Phương trình vô nghiệm')
else:
    x = -b/a
    print(f'Phương trình có một nghiệm {x}')