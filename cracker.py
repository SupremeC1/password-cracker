import hashlib

# Target password to crack (MD5 hash of "letmein")
target_hash = "0d107d09f5bbe40cade3de5c71e9e9b7"

try:
    with open("wordlist.txt", "r") as file:
        for word in file:
            word = word.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            if hashed_word == target_hash:
                print(f"[+] Password found: {word}")
                break
        else:
            print("[-] Password not found in wordlist.")
except FileNotFoundError:
    print("[-] Wordlist file not found. Please check the filename.")
    
    
