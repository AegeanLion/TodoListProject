#imports
import hashlib
import re

#this asks user for a valid email address
email_validation_pattern = ""
def signp(email, password, confirm_password):
    real_email = False
    while not real_email:
        if re.match(email_validation_pattern, email):
            real_email = True
        else:
            return "Please Enter a Valid Email Address"

    if confirm_password == password:
        email_encode = email.encode()
        password_encode = confirm_password.encode()

        password_hash = hashlib.sha256(password_encode).hexdigest()
        email_hash = hashlib.sha256(email_encode).hexdigest()

        with open("credentials.txt", "w") as file:
            file.write(email_encode + ";" + password_encode + "\n")
        file.close()
        
        return "User Registered Successfully"
    else:
        return "Passwords do not match!"


#todo: make the regex valid email identification work
