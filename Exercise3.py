import random
number = random.randint(0, 20)
guess = 0
print("A random number is generated between 0 and 20. Please type your guess.")
while guess != number:
    guess = int(input("Your guess = "))
    if guess < number:
        print("Please increase your guess and try again.")
    elif guess > number:
        print("Please decrease your guess and try again.")
    else:
        print("Congratulations! You guessed it right.")