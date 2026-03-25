from analyzer import analyze_password
from generator import generate_wordlist
from utils import save_wordlist, log_result

# Password analysis
password = input("Enter password to analyze: ")
result = analyze_password(password)

print("\nPassword Strength Score:", result["score"])
print("Feedback:", result["feedback"])

log_result(f"{password} -> {result['score']}")

# Wordlist generation
print("\n--- Generate Custom Wordlist ---")
name = input("Enter name: ")
dob = input("Enter DOB: ")
pet = input("Enter pet name: ")

words = generate_wordlist(name, dob, pet)
save_wordlist(words)

print("Wordlist saved in wordlists/custom.txt")
