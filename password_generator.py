import random
import string


def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):

    characters = ""
    if use_letters:
        characters += string.ascii_letters  # A-Z, a-z
    if use_numbers:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation  # !@#$%^&* etc.

    # Ensure there's at least one type of character selected
    if not characters:
        print("❌ Error: You must select at least one character type!")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔹 Welcome to the Random Password Generator 🔹")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("❌ Error: Password length must be greater than zero.")
            return

        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print(f"\n🔐 Generated Password: {password}")

    except ValueError:
        print("❌ Error: Please enter a valid numeric password length.")


if __name__ == "__main__":
    main()
