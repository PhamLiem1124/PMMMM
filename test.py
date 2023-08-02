n = int(input("Nhap so mon: "))
t = int(input("Nhap thue: "))
t = 1 + t/100
mon = []
for i in range(n):
    m = int(input("Nhap so luong mon thu " + str(i + 1) + ": "))
    mon.append(m)
gia = []
for i in range(n):
    m = int(input("Nhap gia tien mon thu " + str(i + 1) + ": "))
    gia.append(m)

tt = 0
for i in range(n):
    tt += mon[i]*gia[i]
tt *= t
print("Tong tien: " + str(tt) )
    
