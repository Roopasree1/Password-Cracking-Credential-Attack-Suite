import os
from colorama import Fore, Style, init

init()

def banner():
    print(Fore.GREEN + """
 ██████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
██║     ███████║███████╗█████╗
██║     ██╔══██║╚════██║██╔══╝
╚██████╗██║  ██║███████║███████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝

Password Cracking & Credential Attack Suite
Cybersecurity Toolkit
""" + Style.RESET_ALL)


def menu():
    while True:
        print(Fore.CYAN + "\n===== MAIN MENU =====" + Style.RESET_ALL)
        print("1. Generate Dictionary")
        print("2. Password Strength Analyzer")
        print("3. Brute Force Simulator")
        print("4. Hash Identifier")
        print("5. Exit")

        choice = input(Fore.YELLOW + "\nSelect option: " + Style.RESET_ALL)

        if choice == "1":
            os.system("python3 dictionary_generator/generator.py")

        elif choice == "2":
            os.system("python3 password_strength_analyzer/strength_checker.py")

        elif choice == "3":
            os.system("python3 brute_force_simulator/brute_force.py")

        elif choice == "4":
            os.system("python3 hash_identifier/hash_identifier.py")

        elif choice == "5":
            print(Fore.RED + "Exiting toolkit..." + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid option!" + Style.RESET_ALL)


banner()
menu()
