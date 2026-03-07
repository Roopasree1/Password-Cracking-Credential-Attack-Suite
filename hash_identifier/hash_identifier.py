import re

def identify_hash(hash_value):

    if hash_value.startswith("$y$"):
        return "yescrypt"

    elif hash_value.startswith("$1$"):
        return "MD5-Crypt"

    elif hash_value.startswith("$2a$") or hash_value.startswith("$2b$"):
        return "bcrypt"

    elif hash_value.startswith("$5$"):
        return "SHA256-Crypt"

    elif hash_value.startswith("$6$"):
        return "SHA512-Crypt"

    elif re.fullmatch(r"[a-fA-F0-9]{32}", hash_value):
        return "MD5"

    elif re.fullmatch(r"[a-fA-F0-9]{40}", hash_value):
        return "SHA1"

    elif re.fullmatch(r"[a-fA-F0-9]{64}", hash_value):
        return "SHA256"

    else:
        return "Unknown Hash Type"


hash_input = input("Enter hash value: ")

hash_type = identify_hash(hash_input)

print("Detected Hash Type:", hash_type)

print("\nSuggested Attack Method:")

if hash_type in ["MD5", "SHA1", "SHA256"]:
    print("Use dictionary attack with Hashcat")

elif hash_type == "MD5-Crypt":
    print("Use: hashcat -m 500")

elif hash_type == "SHA512-Crypt":
    print("Use: hashcat -m 1800")

elif hash_type == "yescrypt":
    print("Use John the Ripper (yescrypt supported)")

elif hash_type == "bcrypt":
    print("Use John the Ripper or Hashcat (slow hash)")

else:
    print("Manual analysis required")

