import random

min_number = 1
max_number = 10
max_guesses = 3
game_over = False

number = random.randint(min_number, max_number)
current_guess = 0

def get_guess(min: int, max: int) -> str:
	text = "I've thought of a number between " + str(min) + " and " + str(max) + ". Can you guess it? Enter a number:"

	return input(text)


def validate_guess(guess: str, min_number: int, max_number: int) -> bool: 
	is_valid = False
	if guess.isnumeric():
		guess = int(guess)
		if guess >= min_number and guess <= max_number:
			is_valid = True
		else:
			print("Your guess is out of range")	
	else:
		print("That's not a valid integer")

	return is_valid


while not game_over:

	guess = get_guess(min_number, max_number)

	if validate_guess(guess, min_number, max_number):
		guess = int(guess)
		current_guess = current_guess + 1
		if guess == number:
			print("You win! The number was " + str(number))
			game_over = True
		else:
			if current_guess == max_guesses:
				print("Out of guesses. you lose! The number was " + str(number))
				game_over = True
			else:
				if guess < number:
					hint = 'higher'
				else:
					hint = 'lower'

				print("Nope! The number I'm thinking of is " + hint + ". Guess again! You have " + str(max_guesses - current_guess) + " guesses left.")