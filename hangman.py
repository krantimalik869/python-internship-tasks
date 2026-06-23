import random

# List of 5 predefined words
WORDS = ["python", "hangman", "coding", "laptop", "science"]

def display_state(word, guessed_letters, wrong_guesses):
    # Show the word with blanks
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display}")
    print(f"Wrong guesses left: {6 - wrong_guesses}")
    print(f"Incorrect letters: {', '.join(sorted(guessed_letters - set(word))) or 'None'}")

def draw_hangman(wrong_guesses):
    stages = [
        # 0 wrong
        """
   -----
   |   |
       |
       |
       |
       |
=========""",
        # 1 wrong
        """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
        # 2 wrong
        """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
        # 3 wrong
        """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
        # 4 wrong
        """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
        # 5 wrong
        """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
        # 6 wrong - game over
        """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========""",
    ]
    print(stages[wrong_guesses])

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("=" * 40)
    print("      Welcome to HANGMAN!")
    print("=" * 40)
    print(f"Guess the word! It has {len(word)} letters.")

    while wrong_guesses < max_wrong:
        draw_hangman(wrong_guesses)
        display_state(word, guessed_letters, wrong_guesses)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You WON! The word was: '{word}'")
            break

        # Get player input
        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")

    else:
        # Loop ended because wrong_guesses == max_wrong
        draw_hangman(wrong_guesses)
        print(f"\n💀 Game Over! The word was: '{word}'")

    # Ask to play again
    again = input("\nPlay again? (yes/no): ").lower().strip()
    if again in ("yes", "y"):
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    play_hangman()
