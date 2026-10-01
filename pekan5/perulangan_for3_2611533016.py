# Buat file dengan nama perulangan_for3_nim.py
# Buat program untuk perulangan for dalam python 
# Nama variabel ditambah 4 digit nim terakhir contoh:ulang_1234
# program ini menggunakan fungsi input()

ulang_3016 = int(input("Masukkan jumlah_3016 perulangan: "))

jumlah_3016=0
for i_3016 in range(1, ulang_3016 + 1):
    print(i_3016, end=" ")
    jumlah_3016 = jumlah_3016 + i_3016

    if i_3016 < ulang_3016:
        print(" + ", end="")
    else:
        print(" = ", jumlah_3016, end="")
print()
print("jumlah_3016 =", jumlah_3016)