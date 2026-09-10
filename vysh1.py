import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess a number (1-10): "))
    if guess < number:
        print("Too lowwww!ok")
    elif guess > number:
        print("Too high!")

print("You got it!")
