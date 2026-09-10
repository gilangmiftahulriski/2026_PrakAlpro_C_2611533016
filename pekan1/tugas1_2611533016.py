nama = input("Masukkan Nama : ")
tugas = int(input("Masukkan Nilai Tugas : "))
uts = int(input("Masukkan Nilai UTS : "))
uas = int(input("Masukkan Nilai UAS : "))

nilai_akhir = (tugas * 30 + uts * 30 + uas * 40) / 100

if nilai_akhir >= 85:
    predikat = "A"
elif nilai_akhir >= 70:
    predi = "B"
elif nilai_akhir >= 60:
    predikat = "C"
elif nilai_akhir >= 50:
    predikat = "D"
else:
    predikat = "E"

print("====== HASIL NILAI ======")
print("Nama           : ", nama)
print("Nilai Tugas    : ", tugas)
print("Nilai UTS      : ", uts)
print("Nilai UAS      : ", uas)
print("Nilai Akhir    : ", nilai_akhir)
print("Predikat       : ", predikat)