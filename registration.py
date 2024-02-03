import hashlib
import re

email_validation_pattern = ""
def signp():
    real_email = False
    while not real_email:
        email_input = input("Enter Valid Email Address: ")
        if re.match(email_validation_pattern, email_input):
            real_email = True
        else:
            print("\nPlease Enter a Valid Email Address\n")

    password = input("\nEnter Password")
    confirm_password = input("\nConfirm Password")

    if confirm_password == password:
        email_encode = email_input.encode()
        password_encode = confirm_password.encode()

        password_hash = hashlib.sha256(password_encode).hexdigest()
        email_hash = hashlib.sha256(email_encode).hexdigest()

        with open("credentials.txt", "w") as file:
            file.write(email_encode + ";" + password_encode)
        file.close()

        print("\nUser Registered Successfully")
    else:
        print("\nPasswords do not match!")
