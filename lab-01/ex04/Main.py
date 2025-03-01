from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("Chương trình quản lý sinh viên")
    print("**********MENU**********")
    print("** 1. Thêm sinh viên")
    print("** 2. Cập nhật thông tin sinh viên bởi ID")
    print("** 3. Xóa sinh viên bởi ID")
    print("** 4. Tìm kiếm sinh viên theo tên")
    print("** 5. Sắp xếp sinh viên theo điểm trung bình")
    print("** 6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("** 7. Hiển thị danh sách sinh viên")
    print("** 0. Thoát")
    print("************************")
    
    key = int(input("Nhập lựa chọn của bạn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công.")
        
    elif (key == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên bởi ID")
            ID = int(input("Nhập ID sinh viên cần cập nhật: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên rỗng!")
    
    elif (key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên bởi ID")
            ID = int(input("Nhập ID sinh viên cần xóa: "))
            if(qlsv.deleteSinhVien(ID)):
                print("\nSiinh viên có ID = ", ID, "đã bị xóa")
            else:
                print("\nSinh viên có ID = ", ID, "không tồn tại")
        else:
            print("\nDanh sách sinh viên rỗng!")
            
    elif (key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên")
            name = input("Nhập tên sinh viên cần tìm: ")
            searchResault = qlsv.findByName(name)
            qlsv.showSinhVien(searchResault)
        else:
            print("\nDanh sách sinh viên rỗng!")
            
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng!")
            
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng!")
    
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên rỗng!")
    
    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình")
        break
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn lại!")
    
    