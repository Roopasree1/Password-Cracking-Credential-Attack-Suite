import itertools

def generate_dictionary(name, year, pet):
    numbers = ["123", "1234", "007", "2024", "2025"]
    symbols = ["!", "@", "#"]

    passwords = []

    # Basic patterns
    passwords.append(name)
    passwords.append(name + year)
    passwords.append(name.capitalize() + year)

    # Name + numbers
    for num in numbers:
        passwords.append(name + num)
        passwords.append(name.capitalize() + num)

    # Name + symbols
    for sym in symbols:
        passwords.append(name + sym)
        passwords.append(name.capitalize() + sym)

    # Pet combinations
    passwords.append(pet)
    passwords.append(pet + year)
    passwords.append(pet + "123")

    return passwords


def save_wordlist(passwords, filename="generated_wordlist.txt"):
    with open(filename, "w") as f:
        for pwd in passwords:
            f.write(pwd + "\n")

    print("\nWordlist generated successfully!")
    print("Saved as:", filename)
    print("Total passwords:", len(passwords))


def main():
    print("=== Dictionary Generator ===")

    name = input("Enter target name: ")
    year = input("Enter birth year or important year: ")
    pet = input("Enter pet name (optional): ")

    passwords = generate_dictionary(name, year, pet)
    save_wordlist(passwords)


if __name__ == "__main__":
    main()
