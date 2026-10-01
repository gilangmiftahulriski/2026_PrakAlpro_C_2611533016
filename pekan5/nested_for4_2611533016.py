




tinggi_3016 = int(input("Masukkan tinggi pada bilangan genap,misal 10: "))

if tinggi_3016 % 2 != 0:
    print("tinggi harus bilangan genap!")
else:
    a = tinggi_3016
    c = a
    lebar_3016 = (2 * tinggi_3016) - 1

    for i_3016 in range(1, tinggi_3016 + 1):
        b = c + 1

        for j_3016 in range(1, lebar_3016 + 1):

            # Baris atas dan bawah
            if i_3016 == 1 or i_3016 == tinggi_3016:
                if j_3016 == 1 or j_3016 == lebar_3016:
                    print("a", end="")
                else:
                    print("*", end="")

            # Baris isi
            else:
                if j_3016 == 1 or j_3016 == lebar_3016:
                    print("|", end="")
                else:
                    if j_3016 == c:
                        print("<", end="")
                    elif j_3016 == b:
                        print(">", end="")
                    elif j_3016 == (lebar_3016 - c):
                        print("<", end="")
                    elif j_3016 == (lebar_3016 - c + 1):
                        print(">", end="")
                    elif j_3016 > b and j_3016 < (lebar_3016 - c):
                        print(".", end="")
                    else:
                        print("", end="")

        print()

        # Logika asli java
        a -= 2

        if a <= 0:
            c = (-a) + 2
        else:
            c= a