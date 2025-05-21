def password_strength():
    password = input("Enter a password: ")
    edit = ["Your password needs at least"]
    if len(password) <= 7:
        edit.append(" 8 characters")
    if not any(c.isupper() for c in password):
        edit.append(" one uppercase letter")
    if not any(c.islower() for c in password):
        edit.append(" one lowercase letter")
    if not any(c.isdigit() for c in password):
        edit.append(" one digit")
    if not any(not c.isalnum() for c in password):
        edit.append(" one special character")

    if len(edit) == 1:
        statement = "Your password is strong! 💪"
    else:
        statement = ""
        for i in range(len(edit)):
            if i == 0:
                statement += edit[i]
            elif i == len(edit) - 1:
                statement += edit[i] + "."
            else:
                statement += edit[i] + " and"

    print(statement)