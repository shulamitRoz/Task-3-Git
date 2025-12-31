def is_strong_password(password):
    if len(password) < 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if not (has_lower and has_upper and has_digit and has_special):
        return False

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False

    for i in range(len(password) - 2):
        if (
            ord(password[i + 1]) == ord(password[i]) + 1 and
            ord(password[i + 2]) == ord(password[i]) + 2
        ):
            return False

    return True


#קלט מהמשתמש
password = input("הכנס סיסמה לבדיקה: ")

if is_strong_password(password):
    print("הסיסמה תקינה וחזקה ✅")
else:
    print("הסיסמה אינה עומדת בקריטריונים ❌")
