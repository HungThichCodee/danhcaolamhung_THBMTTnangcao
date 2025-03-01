SoGioLam = float(input("nhap so gio lam moi tuan: "))
LuongGio = float(input("nhap thu lao tren moi gio lam tieu chuan: "))
GioTieuChuan = 44
GioVuotChuan = max(0, SoGioLam - GioTieuChuan)
ThucLinh = GioTieuChuan * LuongGio + GioVuotChuan * LuongGio * 1.5
print("so tien thuc linh cua nhan vien: ",ThucLinh)