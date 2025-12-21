def soLonNhat(a, b, c):
    if a >= b and a>= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
def soBeNhat(a, b, c):
    if a <= b and a<= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
so_lon = soLonNhat(10, 5, 8)
so_be = soBeNhat(10, 5, 8)
print(f'Số lớn nhất là: {so_lon}')
print(f'Số bé nhất là: {so_be}')