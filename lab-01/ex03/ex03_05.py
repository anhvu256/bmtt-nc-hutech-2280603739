def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

#Nhập list từ bàn phím
input_list = (input("Nhập danh sách các từ, cách nhau bằng dấu cách: "))
word_list = input_list.split()

#sử dụng hàm và in kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)