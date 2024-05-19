import random

min_number = 1
max_number = 10
max_guesses = 3
game_over = False

number = random.randint(min_number, max_number)
current_guess = 0

while not game_over:

	is_valid = False
	while not is_valid:
		guess = input("I've thought of a number between " + str(min_number) + " and " + str(max_number) + ". Can you guess it? Enter a number:")
		if guess.isnumeric():
			guess = int(guess)
			if guess >= min_number and guess <= max_number:
				is_valid = True
			else:
				print("Your guess is out of range")	
		else:
			print("That's not a valid number?")

	if is_valid:
		current_guess = current_guess + 1
		if guess == number:
			print("You win! The number was " + str(number))
			game_over = True
		else:
			if current_guess == max_guesses:
				print("Out of guesses. you lose! The number was " + str(number))
				game_over = True
			else:
				print('Nope! guess again')
				# improvement: add number of remaining guesses
