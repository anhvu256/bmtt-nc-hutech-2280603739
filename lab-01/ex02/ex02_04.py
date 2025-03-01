#Tạo một danh sách rỗng
j=[]
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        #Thêm số i vào danh sách
        j.append(str(i))
print(','.join(j))