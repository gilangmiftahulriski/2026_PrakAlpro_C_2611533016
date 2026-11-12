first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())



full_name = "Gilang Miftahul Riski"
nim = "2611533016"

# menghapus spasi di awal dan di akhir
clean = full_name.strip()

# mencari spasi pertama
pos = clean.find(" ")

# mengambil nama depan
if pos == -1:
    first_name = clean
else:
    first_name = clean[:pos]

# membuat username
username = first_name.lower() + nim[-3:] 

print(username)
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
