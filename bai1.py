# danh cao lam hung
#Viết một chương trình để tính tổng của tất cả các số chẵn trong một List. 

def tinhTongSoChan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("nhap danh sach cac so cach nhau bang dau phay")
numbers = list(map(int, input_list.split(',')))

print("tong cac so chan trong lst la: ",tinhTongSoChan(numbers))