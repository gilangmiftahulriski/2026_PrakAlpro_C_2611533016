# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh:  jari_3016

from typing import Final
PI_3016: Final = 3.14
print("pi: %f" % (PI_3016))
jari_3016 = float(input("Masukkan nilai jari-jari: "))
luas_3016 = PI_3016 * jari_3016 * jari_3016
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3016, luas_3016))