def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập vào một List từ bàn phím
input_list = input("Nhập vào các phần tử của List, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple được tạo từ List là:", my_tuple)