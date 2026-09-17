# Buat file dengan nama Logika_2611533016.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_3016
# Program ini menggunakan fungsi input()
# Progarm operator logika dalam python

# Memasukkan nilai boolean 
# Input tidak peka terhadap huruf besar dan kecil
a1_3016 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3016 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3016)
print("\nA2 =", a2_3016)

# Konjungsi: bernilai True jika keduanya True
hasil_3016 = a1_3016 and a2_3016
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3016)

# Disjungsi: bernilai True jika salah satunya True
hasil_3016 = a1_3016 or a2_3016
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3016)

# Negasi A1: membalik nilai A1
hasil_3016 = not a1_3016
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3016)

# Negasi A2: membalik nilai A2
hasil_3016 = not a2_3016    
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3016)

# XOR: bernilai True jika kedua nilai berbeda
hasil_3016 = a1_3016 != a2_3016
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3016)