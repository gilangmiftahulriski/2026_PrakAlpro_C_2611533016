# Buat file dengan nama if2_NIM.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_3016
# Program ini menggunakan fungsi input()

umur_3016 = int(input("Input Umur Anda: "))
sim_3016 = input("Apakah Anda Sudah Punya Sim C (y//t):")[0]

if umur_3016 >= 17 and sim_3016 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3016 >= 17 and sim_3016 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3016 < 17 and sim_3016 == 'y':
    print("Anda Belum cukup umur punya SIM")

if umur_3016 < 17 and sim_3016 != 'y':
    print("Anda belum cukup umur bawa motor")