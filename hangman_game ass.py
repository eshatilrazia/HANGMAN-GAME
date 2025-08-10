import random

# 🎯 Predefined list of words
words = ["python", "hangman", "banana", "laptop", "keyboard"]

# 🎲 Randomly choose a word
secret_word = random.choice(words)
guessed_letters = []  # Store correctly guessed letters
wrong_guesses = 0
max_wrong = 6

print("\n🎉 Welcome to Hangman! 🎯")
print("I have chosen a word. Try to guess it one letter at a time!")
print(f"You have {max_wrong} chances. Good luck!\n")

# Function to display current progress
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Game loop
while wrong_guesses < max_wrong:
    print("\nWord:", display_word())
    guess = input("Enter a letter: ").lower()

    # ✅ Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("🔄 You already guessed that letter.")
        continue

    # Check guess
    if guess in secret_word:
        guessed_letters.append(guess)
        print(f"✅ Good guess! '{guess}' is in the word.")
    else:
        wrong_guesses += 1
        print(f"❌ Oops! '{guess}' is not in the word.")
        print(f"Remaining attempts: {max_wrong - wrong_guesses}")

    # Win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

# Lose condition
if wrong_guesses == max_wrong:
    print("\n💀 Game Over! The word was:", secret_word)
