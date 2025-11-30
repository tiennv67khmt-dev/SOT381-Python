so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
for ten, sl in zip(ten_san_pham, so_luong):
    if sl < 10:
        print(f'sản phẩm cần nhập thêm: {ten}')