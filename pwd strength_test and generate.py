import string, secrets

def test_strength(password):
    score = 0
    if len(password) > 8: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    strength = test_strength(pwd)
    print("Strength:", strength)

    if strength != "Strong":
        choice = input("Your password is not strong. Do you want to generate a strong password? (yes/no): ").strip().lower()
        if choice == "yes":
            while True:
                try:
                    length = int(input("Enter password length ex.11 or 15 (min 8): "))
                    if length < 8:
                        print("Please enter a number >= 8.")
                        continue
                    strong_pwd = generate_password(length)
                    print("Generated strong password:", strong_pwd)
                    print("Strength:", test_strength(strong_pwd))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number >= 8.")
        else:
            user_pwd = input("Enter your desired password: ")
            print("Strength of your password:", test_strength(user_pwd))
    else:
        print("Your password is strong!")
        choice = input("Do you want to generate an even stronger password? (yes/no): ").strip().lower()
        if choice == "yes":
            while True:
                try:
                    length = int(input("Enter password length ex.11 or 15 (min 8): "))
                    if length < 8:
                        print("Please enter a number >= 8.")
                        continue
                    strong_pwd = generate_password(length)
                    print("Generated strong password:", strong_pwd)
                    print("Strength:", test_strength(strong_pwd))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number >= 8.")
