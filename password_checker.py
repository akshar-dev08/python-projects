password = input("Enter the password: ")
length = len(password)
has_number = any(char.isdigit()for char in password)
has_upper = any(char.isupper()for char in password)
has_special = any(not char.isalnum()for char in password)

if length <6:
    print("Too! short Weak password !")
elif length>=6 and has_number and has_upper and has_special:
    print("Strong password!")
elif length>= 6 and has_number :
    print("low! Add a capital letter and a special character!")
elif length>= 6 and has_upper:
    print("low! add a number and a special character!")
elif length >= 6 and has_special:
    print("low! add number and capital letter!")
else:
    print("weak! add a number,capital letter and a special character!")
