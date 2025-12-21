ds = [1, 2, 'x', 3, 4, 5, 'x', 6, 7, 8, 'x', 9]
for i in ds:
    if i == 'x':
        ds.remove(i)
print(ds)