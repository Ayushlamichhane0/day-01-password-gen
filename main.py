import secrets
import string


def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return

        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()

