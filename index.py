def pwd_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase :
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    return strength


def strength(password):

    strength = pwd_strength(password)

    if  strength == 5:
        print("The Password is strong. You're safe from Brute Force Attacks !")
    elif  strength >= 3:
        print("The Strength of the Password is Medium.")
    else:
        print("The Password is weak, consider changing it.")


pwd = input("Enter The Password (Min 4 Characters and Max 16 Characters) : ")
print()
if len(pwd) > 16 or len(pwd) < 4:
    print("Password Must Be in Range of 4 to 16 characters")
else:
    print()
    strength(pwd)