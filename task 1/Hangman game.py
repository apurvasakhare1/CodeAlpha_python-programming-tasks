import random

# Step 1: List of predefined words
words = ["apple", "banana", "grapes", "orange", "mango"]

# Step 2: Choose a random word
word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
tries = 6   # maximum incorrect guesses allowed

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Step 4: Game loop
while tries > 0:
    
    # Step 5: Display the current state of the word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    # Step 6: Check if the word is fully guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break

    # Step 7: Take user input
    guess = input("Guess a letter: ").lower()

    # Step 8: Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Step 9: Add guess to guessed letters
    guessed_letters.append(guess)

    # Step 10: Check correct or wrong guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        tries -= 1
        print("❌ Wrong guess! Tries left:", tries)

# Step 11: Game over condition
if tries == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)
