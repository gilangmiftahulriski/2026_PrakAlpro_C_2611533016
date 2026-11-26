n = int(input())

kas = {}

for i in range(n):
    data = input().split()
    nama = data[0]
    if data[1] == "X":
        nominal = 11000
    else:
        nominal = int(data[1])

    if nama in kas:
        kas[nama] += nominal
    else:
        kas[nama] = nominal

# Menampilkan total setoran setiap mahasiswa
for nama, total in kas.items():
    print(f"{nama}: {total}")

# Menghitung total seluruh kas
total_cash = sum(kas.values())
print(f"Total cash: {total_cash}")

# Mencari penyetor terbesar
top_name = None
top_total = -1

for nama, total in kas.items():
    if total > top_total:
        top_name = nama
        top_total = total

print(f"Top contributor: {top_name} ({top_total})")