import random
import string
import argparse

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one type of characters to generate a password.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("--letters", action="store_true", help="Include letters in the password")
    parser.add_argument("--numbers", action="store_true", help="Include numbers in the password")
    parser.add_argument("--symbols", action="store_true", help="Include symbols in the password")
    args = parser.parse_args()

    password = generate_password(args.length, args.letters, args.numbers, args.symbols)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()


# To run the program use this command: python passwordgen.py length of the password and the character to use(letters, numbers, symbols)
# python passwordgen.py 10 --letters --numbers --symbols
# python passwordgen.py 10 --letters --numbers
# python passwordgen.py 10 --letters
# python passwordgen.py 10 --letters --symbols
# python passwordgen.py 10 --numbers --symbols