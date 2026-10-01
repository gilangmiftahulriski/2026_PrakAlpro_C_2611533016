tinggi_3016 = int(input("Masukkan tinggi segitiga: "))

for i_3016 in range(1, tinggi_3016 + 1):

    for j_3016 in range(tinggi_3016 - i_3016):
        print("", end=" ")

    for j_3016 in range(i_3016):
        print("*", end=" ")

    print() 