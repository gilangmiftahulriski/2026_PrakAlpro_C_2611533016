students = input("Masukkan nomor absen kelas: ").split()
submitted_list = input("Masukkan nomor yang mengumpulkan: ").split()

all_students = set(students)
submitted = set(submitted_list)

not_submitted = all_students - submitted

print("Submitted:", len(all_students & submitted), "students")
print("Not submitted:", len(not_submitted), "students")

for student in students:
    if student in not_submitted:
        print(student)
