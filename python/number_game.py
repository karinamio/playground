import random

def number_game():
	total_guesses = 7
	guess_list = []
	number = random.randint(1,100)
	while (True):
		if total_guesses <= 0:
			print("Jokes, you've used up all your chances. My number was {}.".format(number))
			break	
		guess = input("Pick a number between 1 and 100: ")
		total_guesses = total_guesses - 1
		try:
			player_guess = int(guess)
		except:
			print("That's not even a whole number...")
		if player_guess in guess_list:
			print("You guessed that already. You have {} chances left.".format(total_guesses))
		else:
			guess_list.append(player_guess)
			if player_guess == number:
				print("Wow, congrats! You got it. The number was {}.".format(number))
				break
			else:
				if player_guess < number:
					print("Hmm, try something higher. You have {} chances left.".format(total_guesses))
				else:
					print("Hmm, try something lower. You have {} chances left.".format(total_guesses))
		continue

number_game()
