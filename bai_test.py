# viết số trung bình cộng của 3 số nguyên a, b, c
a = int(input('nhập số a: '))
b = int(input('nhập số b: '))
c = int(input('nhập số c: '))
trung_binh = (a + b + c) / 3
print(f'Trung bình cộng của {a}, {b}, {c} là: {trung_binh}')


# viết chương trình nhập vào số nguyên, cho biết số đó có đồng thời chia hết cho 3 và 5 hay không ?
n = int(input('nhập vào một số: '))
if n % 3 == 0 and n % 5 == 0:
    print('chia hết cho 3 và chia hết cho 5')
else: 
    print('không chia hết cho 3 và 5')