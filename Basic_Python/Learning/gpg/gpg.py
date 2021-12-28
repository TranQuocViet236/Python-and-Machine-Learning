t = int(input("Nhập số giây:"))
h = t//3600
p = (t % 3600)//60
s = (t % 3600) % 60
print("Kết quả là:",h,":",p,":",s)