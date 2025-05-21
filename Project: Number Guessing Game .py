import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = 0
    attempts = 0
    while guess != number_to_guess:
        guess = int(input("Guess the number (between 1 and 100): "))
        if guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        attempts += 1
        if attempts == 10:
            print("Game over! Better luck next time!")
            return
    print("Congratulations! You guessed it in", attempts, "attempts!")


number_guessing_game()