# 🔐 Simple Password Cracker (Python)

This project demonstrates how a dictionary-based password cracker works using Python.  
It compares hashed passwords to a list of common password guesses.

---

## 📁 Files Included

- `cracker.py` – Main script that runs the password cracker
- `wordlist.txt` – List of possible password guesses
- `screenshot.png` – (Optional) Screenshot of the program running in IDLE

---

## ⚙️ How It Works

- The script uses `hashlib` to hash words from `wordlist.txt`
- It compares each hash to a target hash
- If a match is found, the password is "cracked" and printed

---

## ▶️ How to Run

1. Make sure `cracker.py` and `wordlist.txt` are in the same folder
2. Open `cracker.py` in Python IDLE
3. Press `F5` or click **Run > Run Module**
4. See if the password is found!

---

## 🧠 What I Learned

- How password hashing works
- How to use `hashlib` in Python
- The basics of dictionary attacks and password security

---
