n = int(input("Nhập số phần tử của danh sách: "))
ds = []
for i in range(n):
    a = input(f'nhập phần tử thứ {i}: ')
    ds.append(a)
print(f'danh sách ban đầu: {ds}')
ds.sort()
print(f'danh sách sau khi sắp xếp: {ds}')