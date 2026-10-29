# Password Generator

A lightweight, secure command-line password generator written in Python. It generates randomized passwords of any specified length using standard alphanumeric characters and punctuation symbols.

## Features

- **Cryptographically Secure**: Built with Python's standard [`secrets`](https://docs.python.org/3/library/secrets.html) module, designed specifically for managing secrets and generating tokens/passwords (unlike the standard `random` module, which is pseudo-random and predictable).
- **High Entropy & Character Diversity**: Combines uppercase letters, lowercase letters, digits, and punctuation symbols (`string.ascii_letters`, `string.digits`, and `string.punctuation`).
- **Input Validation**: Gracefully handles non-integer input and non-positive length requests.
- **Zero Dependencies**: Relies exclusively on Python's built-in standard library.

## Requirements

- Python 3.6+

## Getting Started

### 1. Clone or Open the Repository

```bash
cd day-01-password-gen
```

### 2. Run the Script

Execute the script using Python:

```bash
python3 main.py
```

### 3. Example

```text
Enter password length: 16
Generated password: c=^!g<}zDRbJo\}n
```

## How It Works

- **`generate_password(length: int)`**: Aggregates letters, digits, and special characters, then uses `secrets.choice()` to pick characters randomly and uniformly to assemble the final string.
- **`main()`**: Prompts the user for their desired password length, validates the input, and prints the generated password to standard output.

