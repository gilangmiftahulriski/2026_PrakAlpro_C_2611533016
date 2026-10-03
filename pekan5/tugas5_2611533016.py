print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

N_3016 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bingkai atas
print("#", end="")
for bingkai_3016 in range((4 * N_3016) + 5):
    print("=", end="")
print("#")

# Fase 1
for baris_3016 in range(1, N_3016 + 1):
    banyak_3016 = N_3016 - baris_3016 + 1   #Bingung namain apa soalnya kepake buat spasi dan angka mundur sekaligus
    # Bingkai kiri
    print("|", end="")
    print(" ", end="")
    # Spasi kiri
    for spasi_3016 in range(2 * (N_3016 - banyak_3016)):
        print(" ", end="")
    # Angka mundur
    for angka_3016 in range(1, banyak_3016 + 1):
        print(banyak_3016 - angka_3016 + 1, end="")
        print(" ", end="")
    # Tengah
    print("<*>", end="")
    # Angka maju
    for angka_3016 in range(1, banyak_3016 + 1):
        print(" ", end="")
        print(angka_3016, end="")
    # Spasi kanan
    for spasi_3016 in range(2 * (N_3016 - banyak_3016)):
        print(" ", end="")
    # Bingkai kanan
    print(" ", end="")
    print("|")

# Fase 2
print("|", end="")
for spasi_3016 in range(2 * N_3016 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3016 in range(2 * N_3016 + 1):
    print(" ", end="")
print("|")

# Fase 3
for baris_3016 in range(1, N_3016 + 1):
    # Bingkai kiri
    print("|", end="")
    print(" ", end="")
    # Spasi kiri
    for spasi_3016 in range(2 * (N_3016 - baris_3016)):
        print(" ", end="")
    # Angka mundur
    for angka_3016 in range(1, baris_3016 + 1):
        print(baris_3016 - angka_3016 + 1, end="")
        print(" ", end="")
    # Tengah
    print("<*>", end="")
    # Angka maju
    for angka_3016 in range(1, baris_3016 + 1):
        print(" ", end="")
        print(angka_3016, end="")
    # Spasi kanan
    for spasi_3016 in range(2 * (N_3016 - baris_3016)):
        print(" ", end="")
    # Bingkai kanan
    print(" ", end="")
    print("|")