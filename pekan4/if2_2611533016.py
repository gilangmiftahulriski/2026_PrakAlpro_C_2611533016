# Buat file dengan nama if2_NIM.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_3016
# Program ini menggunakan fungsi input()

ipk_3016 = float(input("Input IPK anda = "))

if ipk_3016 > 2.75:
    print("Anda Lulus Sangat Memuaskan Dengan IPK " + str(ipk_3016))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")