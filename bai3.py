# danh cao lam hung
#Viết chương trình để tạo một Tuple từ một List nhập vào từ bàn phím. 

def Tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("nhap danh sach cac so cach nhau bang dau phay")
numbers = list(map(int, input_list.split(',')))

my_tuple = Tao_tuple_tu_list(numbers)
print("list: ",numbers)
print("Tuple tu list: ",my_tuple)


