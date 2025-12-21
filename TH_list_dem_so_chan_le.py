n = int(input("Nhập số lượng phần tử "))
ds = []
for i in range (n):
    tam = int(input(f'Nhập phần tử thứ {i}: '))
    ds.append(tam)
print(ds)

dem_chan = 0
dem_le = 0 
for so in ds:
    if so % 2 == 0:
        dem_chan += 1
    else :
        dem_le += 1
print (f'có {dem_chan} số chẵn')
print (f'có {dem_le} số lẻ')
