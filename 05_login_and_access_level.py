# Login and Access Level
# Use nested conditions to check credentials and display access.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    role = "Administrator"
    print(f"Role: {role}")
    if role == "Administrator":
        print(f"Full system access.")
    elif role == "Teacher":
        print(f"Teacher access.")
    else:
        print(f"Student access.")
elif username == "student12" and password == "study123":
    role = "Student"
    print(f"Role: {role}")
    if role == "Administrator":
        print(f"Full system access.")
    elif role == "Teacher":
        print(f"Teacher access.")
    else:
        print(f"Student access.")
else:
    print(f"Invalid username or password.")
