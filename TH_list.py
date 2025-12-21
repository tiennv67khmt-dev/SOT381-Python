n = int(input('nhập số lượng phần tử: '))
ds = []
for i in range (n):
    tam = int(input(f'nhập phần tử thứ {i}: '))
    k = ds.append(tam)
print('Danh sách các phần tử là: ')
print(ds)
tong = sum(ds)
print(f'Tổng các phần tử trong danh sách là: {tong}')