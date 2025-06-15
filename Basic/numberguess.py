import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Ask the user to guess the number
while True:
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break
