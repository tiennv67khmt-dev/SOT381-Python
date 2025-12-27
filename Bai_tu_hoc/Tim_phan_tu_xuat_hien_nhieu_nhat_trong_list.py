list = [1, 2, 1, 3, 1, 4, 2, 3]
nhieu_nhat = 0
for i in list:
    dem = list.count(i)
    if dem > nhieu_nhat:
        nhieu_nhat = dem
        n = i
print(f'Phần tử {n} xuất hiện nhiều nhất với {nhieu_nhat} lần')