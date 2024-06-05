import random

def guess_the_number():
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        user_guess = input("Enter your guess: ")

        # Check if the input is a number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
