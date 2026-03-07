import itertools
import string

password = "abc"

characters = string.ascii_lowercase

attempts = 0

for combo in itertools.product(characters, repeat=3):
    
    guess = ''.join(combo)
    attempts += 1
    
    print("Trying:", guess)
    
    if guess == password:
        print("\nPassword Found:", guess)
        print("Attempts:", attempts)
        break
