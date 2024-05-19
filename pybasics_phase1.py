import random

number = random.randint(1, 10)

guess = input("I've thought of a number between 1 and 10. Can you guess it? Enter a number:")

if int(guess) == number:
	print("You win! The number was " + str(number))
else:
	print("You lose. The number was " + str(number))