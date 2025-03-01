def dao_nguoc_list(list):
    return list[::-1]

#Nhập danh sách từ người dùng và xử lí chuỗi
input_list = input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ")
numbers = list(map(int, input_list.split(',')))

#sử dụng hàm dao_nguoc_list để đảo ngược danh sách
list_dao_nguoc = dao_nguoc_list(numbers)
print(f"List sau khi đảo ngược là: {list_dao_nguoc}")