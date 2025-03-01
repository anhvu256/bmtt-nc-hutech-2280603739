def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

#Nhập danh sách từ người dùng và xử lí chuỗi
input_list = input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ")
numbers = list(map(int, input_list.split(',')))

#sử dụng hàm tinh_tong_so_chan để tính tổng các số chẵn trong danh sách
tong = tinh_tong_so_chan(numbers)
print(f"Tổng các số chẵn trong danh sách là: {tong}")