# Nhập số từ người dùng
number = int(input("Nhập một số nguyên: "))
# Kiểm tra số vừa nhập có phải số chẵn hay không
if number % 2 == 0:
    print("Số", number, "là số chẵn.")
else:
    print("Số", number, "không phải là số chẵn.")