import random

# Generate a random number between 1 and 20

random_number = random.randint(1, 20)
print(random_number)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 20: "))

# 5 chances to guess the number
for i in range(5):
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! Congratulations! You guessed the correct number! {random_number}.")
        break
    guess = int(input("Guess a number between 1 and 20: "))
else:
    print(f"Sorry, you've used all your chances. The number was {random_number}.")