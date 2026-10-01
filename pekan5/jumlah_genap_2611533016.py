# Buat file dengann nama jumlah_3016_genap_nim.py
# Buat program untuk perulangan for dalam pythobn
# Nama variabel ditambah 4 ddigit terakhir contoh:ulang_1234
# program ini menggunakan fungsi input()

ulang_3016 = int(input("Masukkan nilai batas: "))

jumlah_3016_3016 = 0
for i in range(1, ulang_3016 + 1):
    if i % 2 ==0:
        print(i, end= " ")
        jumlah_3016 = jumlah_3016 + 1

        if i < ulang_3016:
            print(" + ", end="" )
        else:
            print(" = ", jumlah_3016, end="")
print()
print("jumlah_3016 = ", jumlah_3016)
