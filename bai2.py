# danh cao lam hung
#Viết chương trình để đảo ngược vị trí của các phần tử trong một danh sách. 

def DaoNguocViTri(lst):
    return lst[::-1]

input_list = input("nhap danh sach cac so cach nhau bang dau phay")
numbers = list(map(int, input_list.split(',')))

print("list sau khi dao nguoc: ",DaoNguocViTri(numbers))