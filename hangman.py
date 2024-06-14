import random

def display_hangman(wrong_guesses):
    """Displays the hangman visual based on the number of wrong guesses."""
    stages = [
        """
            --------
            |      |
            |
            |
            |
            |
            -------
        """,
        """
            --------
            |      |
            |      O
            |
            |
            |
            -------
        """,
        """
            --------
            |      |
            |      O
            |      |
            |
            |
            -------
        """,
        """
            --------
            |      |
            |      O
            |     /|\\
            |
            |
            -------
        """,
        """
            --------
            |      |
            |      O
            |     /|\\
            |     /
            |
            -------
        """,
        """
            --------
            |      |
            |      O
            |     /|\\
            |     / \\
            |
            -------
        """,
        """
            --------
            |      |
            |      O
            |     /|\\
            |     / \\
            |    /
            -------
        """
    ]
    print(stages[wrong_guesses])

def get_word():
    """Selects a random word from a list of words."""
    words = ["python", "programming", "computer", "science", "machine", "learning"]
    return random.choice(words)

def guess_letter(word, guessed_letters):
    """Checks if the guessed letter is present in the word."""
    correct_guess = False
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    return correct_guess

def main():
    """Main function to run the Hangman game."""
    word = get_word()
    guessed_letters = []
    wrong_guesses = 0
    print("Welcome to Hangman!")

    while True:
        display_hangman(wrong_guesses)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            if all(letter in guessed_letters for letter in word):
                display_hangman(wrong_guesses)
                print(f"You win! The word was: {word}")
                break
        else:
            wrong_guesses += 1
            if wrong_guesses == len(display_hangman.__code__.co_consts[0]) - 1:
                display_hangman(wrong_guesses)
                print(f"You lose! The word was: {word}")
                break

        guess_letter(word, guessed_letters)

if __name__ == "__main__":
    main()
