import random
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
special_letters="!@#$%^&*()-_=+[]{}|;:,.<>?/"
while True:
    try:
        length=int(input("Enter the length for your password: "))
        if length<=0:
            print("please enter a valid positive integer")
        else:
            break
    except ValueError:
        print("Enter a valid integer.")


upper_case=input("Include upper case letters? (yes/no): ").lower()
lower_case=input("Include lower case letters? (yes/no): ").lower()
digit=input("Include digits? (yes/no): ").lower()
special_letters_=input("Include special letters? (yes/no): ").lower()

characters=""
mandatory_characters=[]
if upper_case=="yes":
    characters+=uppercase_letters
    mandatory_characters.append(random.choice(uppercase_letters))
if lower_case=="yes":
    characters+=lowercase_letters
    mandatory_characters.append(random.choice(lowercase_letters))
if digit=="yes":
    characters+=digits
    mandatory_characters.append(random.choice(digits))
if special_letters_=="yes":
    characters+=special_letters
    mandatory_characters.append(random.choice(special_letters))

if not characters:
    print("At least one character type must be selected.")
else:
    password="".join(mandatory_characters)
    while len(password)<length:
        password+=random.choice(characters)
    password_list=list(password)
    random.shuffle(password_list)
    final_password="".join(password_list)
    print(f"Generated password: {final_password}")
