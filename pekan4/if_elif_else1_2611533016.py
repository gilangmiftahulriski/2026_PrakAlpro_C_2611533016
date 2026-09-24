# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_3016
# Program ini menggunakan fungsi input()

umur_3016 = int(input("Input Umur Anda: "))
sim_3016 = input("Apakah Anda Sudah Punya Sim C (y//t):")[0]

if umur_3016 >= 17 and sim_3016 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_3016 >= 17 and sim_3016 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3016 < 17 and sim_3016 == 'y':
    print("Anda Belum cukup umur punya SIM")
else:
    print("anda belum cukup umur dan tidak boleh bawa motor")
print("program selesai")