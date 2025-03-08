#Viết chương trình để đếm số lần xuất hiện của mỗi phần tử trong một List và lưu kết quả vào một Dictionary. 
def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("nhap danh sach cac tu, cach nhau bang dau cach: ")
word_list = input_string.split( )

print("so lan xuat hien cua cac phan tu: ",dem_so_lan_xuat_hien(word_list))