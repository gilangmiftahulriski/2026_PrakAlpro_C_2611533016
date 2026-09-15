print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3016 = input("Masukkan Nama Mahasiswa : ")
kelamin_3016 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3016 = int(input("Masukkan Umur : "))
skor_3016 = float(input("Masukkan Skor Tes Awal : "))

alamat_3016 = """
Kecamatan Pauh,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_3016: Final = 75.0
token_3016 = 100+3j
lulus_3016 = skor_3016 > kkm_3016

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_3016," | ",type(nama_3016))
print("Jenis Kelamin : ",kelamin_3016," | ",type(kelamin_3016))
print("Alamat Domisili : ",alamat_3016," | ",type(alamat_3016))
print("Umur : ",umur_3016," tahun | ",type(umur_3016))
print("Skor Tes Awal : ",skor_3016," | ",type(skor_3016))
print("ID Token Sinyal: ",token_3016," | ",type(token_3016))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_3016," | ",type(kkm_3016))
print("Apakah Dinyatakan Lulus?: ",lulus_3016," | ",type(lulus_3016))