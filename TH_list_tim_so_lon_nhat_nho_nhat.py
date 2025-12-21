ds = []
for i in range (1,11):
    tam = int(input(f'nhập phần tử thứ {i}: '))
    a = ds.append(tam)
print(f'Danh sách các phần tử là: {ds}')
print(f'Số lớn nhất là {max(ds)}')
print(f'Số nhỏ nhất là {min(ds)}')