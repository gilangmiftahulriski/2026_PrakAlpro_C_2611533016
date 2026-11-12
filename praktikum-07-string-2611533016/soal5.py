Username= input("Username: ")

if len(Username) < 5:
    print("Invalid: at least 5 characters")
elif not Username.isalnum():
    print("Invalid: letters and digits only")
elif not Username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")


nim = input("Masukkan NIM: ")

if len(nim) == 10 and nim.isdigit():
    print("Valid")
    print("Intake year 20" + nim[:2])
else:
    print("Invalid NIM")

# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"