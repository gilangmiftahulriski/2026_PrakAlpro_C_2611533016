print("=== SISTEM TRANSAKSI TOKO ===")
nama_3016 = input("Masukkan Nama Pelanggan : ")
status_3016 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_3016 = int(input("Masukkan Total Belanja : "))
jumlah_3016 = int(input("Masukkan Jumlah Barang : "))
promo_3016 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_3016}")
print(f"Status Pelanggan     : {status_3016}")
print(f"Total Belanja        : Rp{total_3016}")
print(f"Jumlah Barang        : {jumlah_3016}")
print(f"Kode Promo           : {promo_3016}")

kode_promo_3016 = ["HEMAT10", "HEMAT20", "HIDUPMAHASISWA", "HIDUPFTI"] #list kode promo

syarat_total_3016 = total_3016 >= 200000 # apakah memenuhi syarat belanja
syarat_jumlah_3016 = jumlah_3016 >= 3 # apakah memenuhi syarat barang
status_valid_3016 = status_3016 == "member" # apakah user member
promo_valid_3016 = promo_3016 in kode_promo_3016 # apakah kode promo ada dalam list

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_total_3016}")
print(f"Jumlah Barang >= 3         : {syarat_jumlah_3016}")
print(f"Status Member              : {status_valid_3016}")
print(f"Kode Promo Tersedia        : {promo_valid_3016}")
print(f"Mendapatkan Diskon         : {syarat_jumlah_3016 or syarat_total_3016}")
print(f"Mendapatkan Promo          : {promo_valid_3016}")

diskon_3016 = 0.05

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                      : Rp{diskon_3016 * total_3016}")
print(f"Total Pembayaran            : Rp{total_3016 - total_3016 * diskon_3016}")
print(f"Rata-rata Harga Barang      : Rp{(total_3016 - total_3016 * diskon_3016)/jumlah_3016}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses              : ...")
print(f"Member Access               : {status_valid_3016}")
print(f"Promo Access                : {promo_valid_3016}")
print(f"Free Shipping Access        : ...")

kode_transaksi_3016 = int(status_valid_3016) << 0 | int(syarat_total_3016) << 1 | int(syarat_jumlah_3016) << 2 | int(promo_valid_3016) << 3
kode_referensi_3016 = int(status_valid_3016) << 0 | int(syarat_total_3016) << 1 | int(promo_valid_3016) << 3

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{format(int(status_valid_3016) << 0,'04b')} | {format(int(syarat_total_3016) << 1,'04b')} | {format(int(syarat_jumlah_3016) << 2,'04b')} | {format(int(promo_valid_3016) << 3,'04b')}")
print(f"Kode Biner   : {format(kode_transaksi_3016,'04b')}")
print(f"Kode Desimal : {kode_transaksi_3016}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_transaksi_3016,'04b')} & {format(int(status_valid_3016) << 0,'04b')}")
print(f"Hasil Biner   : {format((kode_transaksi_3016) & int(status_valid_3016) << 0,'04b')}")
print(f"Hasil Desimal : {(kode_transaksi_3016) & int(status_valid_3016) << 0}")

print("Cek Promo")
print(f"{format(kode_transaksi_3016,'04b')} & {format(int(promo_valid_3016) << 3,'04b')}")
print(f"Hasil Biner   : {format((kode_transaksi_3016) & int(promo_valid_3016) << 3,'04b')}")
print(f"Hasil Desimal : {(kode_transaksi_3016) & int(promo_valid_3016) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_transaksi_3016,'04b')}")
print(f"Kode Referensi : {format(kode_referensi_3016,'04b')}")
print(f"{format(kode_transaksi_3016,'04b')} ^ {format(kode_referensi_3016,'04b')}")
print(f"Hasil Biner   : {format((kode_transaksi_3016) ^ (kode_referensi_3016),'04b')}")
print(f"Hasil Desimal : {(kode_transaksi_3016) ^ (kode_referensi_3016)}")

print("\n=== Shift ===")
print(f"{format(kode_transaksi_3016,'04b')} << 1")
print(f"Hasil Biner   : {format((kode_transaksi_3016) << 1,'04b')}")
print(f"Hasil Desimal : {(kode_transaksi_3016) << 1}") 
print("=== SELESAI ===")