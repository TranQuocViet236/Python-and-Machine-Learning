print("Chương trình kiểm tra năm nhuần")
y = int(input("Mời cu em nhập năm vào đây:"))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("Năm", y, "là năm nhuần")
else :
    print("Năm", y, "là năm không nhuần")