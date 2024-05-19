import random

# improvement 1: add explicit error messages
# improvement 2: convert if statements to a while loop

min_number = 1
max_number = 10
number = random.randint(min_number, max_number)

guess = input("I've thought of a number between " + str(min_number) + " and " + str(max_number) + ". Can you guess it? Enter a number:")


is_valid = True
# message = ''
# is guess a number?
if not guess.isnumeric():
	is_valid = False
	# message = 'Your guess must be a number'

guess = int(guess)

# is guess in range?
if guess < min_number or guess > max_number:
	is_valid = False
	# message = 'Your guess is out of range'

# a better way?

#while not is_valid:
#	if guess.isnumeric():
#		guess = int(guess)
#		if guess >= 1 and guess <= max_number:
#			is_valid = True
#		else:
#			print("omg how are you so dumb, that's out of range?")	
#	else:
#		print("omg how are you so dumb, that's not a valid number?")


if is_valid:
	if int(guess) == number:
		print("You win! The number was " + str(number))
	else:
		print("You lose. The number was " + str(number))
else:
	print("Your guess is not valid")
	# print(message)