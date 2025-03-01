def ChiaHetCho5(SoNhiPhan):  
    SoThapPhan = int(SoNhiPhan, 2)  
    if SoThapPhan % 5 == 0:  
        return True  
    else:  
        return False  

chuoiSoNhiPhan = input("nhap chuoi so nhi phan (phan tach boi dau phay):")  
soNhiPhanList = chuoiSoNhiPhan.split(',')  
SochiaHetCho5 = [so for so in soNhiPhanList if ChiaHetCho5(so)]  

if len(SochiaHetCho5) > 0:  
    KetQua = ','.join(SochiaHetCho5)  
    print("cac so nhi phan chia het cho 5 la:", KetQua)  
else:  
    print("khong co so nhi phan nao chia het cho 5 trong chuoi da nhap")  
