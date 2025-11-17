import math
a = float(input('nhập a: '))
b = float(input('nhập b: '))
c = float(input('nhập c: '))
if a == 0:
    if b == 0:
        print('Phương trình có vô số nghiệm')
    else:
        print('Phương trình vô nghiệm')
else:
    delta = b**2-4*a*c
    x = -b/2*a
    if delta < 0:
        print('Vô nghiệm')
    elif delta == 0:
        print('Có nghiệm kép {x}')
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'Có 2 nghiệm phân biệt {x1}, {x2}')