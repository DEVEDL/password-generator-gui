import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+"

length = int(input("Enter password length (min 4): "))

if length < 4:
    print("Password length should be at least 4!")
else:
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols

    for i in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    final_password = "".join(password)

    print("Strong Password:", final_password)