import random

# 1. Setup Data
words = {
    "easy": ["apple", "train", "money", "india"],
    "medium": ["python", "bottle", "monkey", "planet", "laptop"],
    "hard": ["elephant", "diamond", "umbrella", "computer", "mountain"]
}

print("=== Welcome to the Password Guessing Game! ===")
level = input("Choose difficulty (easy, medium, hard): ").lower()

# 2. Select Word (with a fallback for typos)
if level not in words:
    print("Invalid choice. Defaulting to Easy.")
    level = "easy"

secret = random.choice(words[level])
attempts = 0

print(f"\nI'm thinking of a {len(secret)} letter word. Good luck!")

# 3. Main Game Loop
while True:
    guess = input("\nEnter your guess: ").lower()
    attempts += 1

    # Win Condition
    if guess == secret:
        print(f"✨ Congratulations! You found '{secret}' in {attempts} attempts. ✨")
        break

    # Wrong Guess - Offer a Hint
    print(f"Incorrect! (Attempt {attempts})")

    # Only offer the big hint if they haven't won yet
    show_hint = input("Need a reveal of the first/last letters? (y/n): ").lower()
    if show_hint == 'y':
        print(f"Hint: The word starts with '{secret[0]}' and ends with '{secret[-1]}'")

    # 4. Generate the 'Match' Hint (Visual feedback)
    feedback = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            feedback += guess[i]
        else:
            feedback += "_"

    print(f"Current Progress: {feedback}")

print("\nGame Over. Thanks for playing!")
