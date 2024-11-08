import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Set up the game
    secret_number = random.randint(1, 100)
    attempts = 10  # The player has 10 attempts to guess

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100.")
                continue
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempt} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
