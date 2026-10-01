# Buat file dengan nama nested_for3_nim.py
# Buat program untuk perulangan for dalam python 
# Nama variabel ditambah 4 digit nim terakhir contoh:ulang_1234
# program ini menggunakan fungsi input()

batas_3016 = int(input("Masukkan nilai batas: "))
for i_3016 in range(batas_3016 + 1):
    for j_3016 in range(batas_3016 + 1):
        print(i_3016 + j_3016, end=" ") 
    print() # pindah ke baris berikutnya