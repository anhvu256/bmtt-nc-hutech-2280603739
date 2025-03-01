def remove_key_from_dict(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
updated_dict = remove_key_from_dict(my_dict, key_to_delete)
if updated_dict:
    print("Phần tử đã được xóa: ", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa")