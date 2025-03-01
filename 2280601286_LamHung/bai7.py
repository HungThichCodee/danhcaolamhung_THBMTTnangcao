def ChiaHetCho5(SoNhiPhan):
    SoThapPhan = int(SoNhiPhan, 2)
    if SoThapPhan % 5 == 0:
        return True
    else:
        return False

SoNhiPhan = input("hap mot so nhi phan").strip()
if set(SoNhiPhan) <= {'0','1'}:
    if ChiaHetCho5(SoNhiPhan):
        print("so nhi phan chia het cho 5 la:", SoNhiPhan)
    else:
        print("Không có số nhị phân hợp lệ nào chia hết cho 5.")
else:
    print("ban nhap ko dung dinh dang.")