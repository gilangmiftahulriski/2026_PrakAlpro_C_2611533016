# Buat file dengan nama assignment_2611533016.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_3016
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Progarm operator assignment dalam python

angka1_3016 = int(input("Input angka-1: "))
angka2_3016 = int(input("Input angka-2: "))

print("nilai awal angka1 =", angka1_3016)
print("nilai angka2 =", angka2_3016)

# Assignment biasa
hasil_3016 = angka1_3016
print("\nAssignment Biasa (=)")
print("Hasil =", hasil_3016)

# Assignment penambahan
hasil_3016 = angka1_3016
hasil_3016 += angka2_3016
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil_3016)

# Assignment pengurangan
hasil_3016 = angka1_3016
hasil_3016 -= angka2_3016
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_3016)

# Assignmet perkalian
hasil_3016 = angka1_3016
hasil_3016 *= angka2_3016
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_3016)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3016 != 0:
    hasil_3016 = angka1_3016
    hasil_3016 /= angka2_3016
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil_3016)
    #Operator tambahan
    hasil_3016 = angka1_3016
    hasil_3016 //= angka2_3016
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_3016)
    hasil_3016 = angka1_3016
    hasil_3016 %= angka2_3016
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil_3016)
else:
    print("Pembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3016 = angka1_3016
hasil_3016 **= angka2_3016
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil_3016)
