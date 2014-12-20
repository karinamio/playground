from __future__ import print_function
import random

CELLS = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5),
		 (1,0), (1,1), (1,2), (1,3), (1,4), (1,5),
		 (2,0), (2,1), (2,2), (2,3), (2,4), (2,5),
		 (3,0), (3,1), (3,2), (3,3), (3,4), (3,5),
		 (4,0), (4,1), (4,2), (4,3), (4,4), (4,5)]

def draw_map(player):
	print(" _ _ _ _ _ _")
	tile = "|{}"
	for index, cell in enumerate(CELLS):
		if index in [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28]:
			if cell == player:
				print(tile.format("@"), end = "")
			elif cell == monster:
				print(tile.format("m"), end = "")
			elif cell == door:
				print(tile.format("d"), end = "")
			else:
				print(tile.format("_"), end = "")
		else:
			if cell == player:
				print(tile.format("@|"))
			elif cell == monster:
				print(tile.format("m|"))
			elif cell == door:
				print(tile.format("d|"))
			else:
				print(tile.format("_|"))

def print_instructions():
	print("Welcome to the dungeon.")
	print("You have one and only one mission. Navigate through the dungeon and escape from the door. Watch out for the monsters!")
	print("Enter \"left\", \"right\", \"up\" or \"down\" to move.")
	print("Enter \"help\" for a list of valid game commands.")
	print("Enter \"quit\" to exit the game.")

def get_locations():
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	player = random.choice(CELLS)

	if monster == door or monster == player or door == player:
		return get_locations()

	return monster, door, player

def get_moves(player):
	moves = ["left", "right", "up", "down"]
	if player[0] == 0:
		moves.remove("up")
	if player[0] == 4:
		moves.remove("down")
	if player[1] == 0:
		moves.remove("left")
	if player[1] == 5:
		moves.remove("right")
	return moves

def move_player(player, move):
	x, y = player

	if move == "left":
		y = y - 1
	elif move == "right":
		y = y + 1
	elif move == "up":
		x = x - 1
	elif move == "down":
		x = x + 1
	return x, y


monster, door, player = get_locations()
print_instructions()
while True:
	moves = get_moves(player)
	draw_map(player)

	move = input("> ").lower()

	if move in moves:
		player = move_player(player,move)
	else:
		print("Walls hurt. Stop walking into them.")
		continue

	if player == door:
		print ("Nice, you've successfully escaped!")
		break
	elif player == monster:
		print("You've been slayed. Better luck next time!")
		break
	
	if move == "help":
		print_instructions()
	if move == "quit":
		break