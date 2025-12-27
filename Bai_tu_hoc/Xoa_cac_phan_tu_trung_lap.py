ds = [1, 2, 1, 3, 1, 4, 2, 3]
for i in ds:
    while ds.count(i) > 1:
        ds.remove(i)
print(ds)