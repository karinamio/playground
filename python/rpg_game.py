import sys
from rpg_character import Character
from rpg_monster import Dragon
from rpg_monster import Goblin
from rpg_monster import Troll

class Game:
	def __init__(self):
		self.setup()
		while self.player.hp and (self.monster or self.monsters):
			print("\n" + "=" * 20)
			print(self.player)
			self.monster_turn()
			print("-" * 20)
			self.player_turn()
			self.cleanup()
			print("\n" + "=" * 20)
		if self.player.hp:
			print("You win.")
		elif self.monster or self.monsters:
			print("You lose.")
		else:
			print("Uhhh everyone's dead.")
		sys.exit()

	def setup(self):
		self.player = Character()
		self.monsters = [
			Goblin(),
			Troll(),
			Dragon()
		]
		self.monster = self.get_next_monster()

	def get_next_monster(self):
		try:
			return self.monsters.pop()
		except IndexError or TypeError:
			return None

	def player_turn(self):
		action = input("Would you like to [a]ttack, [r]est or [q]uit?: ").lower()
		if action == "a":
			print("You're attacking {}.".format(self.monster))
			if self.player.attack():
				if self.monster.defend():
					print("{} dodged your attack!".format(self.monster))
				else:
					if self.player.level_up():
						self.monster.hp -= 2
					else:	
						self.monster.hp -= 1
					print("You hit {} with your {}.".format(self.monster, self.player.weapon))
			else:
				print("You missed!")
		elif action == "r":
			self.player.rest()
		elif action == "q":
			print("Thanks for playing.")
			sys.exit()
		else:
			self.player_turn()

	def monster_turn(self):
		if self.monster.attack():
			print("Watch out! You're being attacked by {}.".format(self.monster))
			action = input("Wanna dodge the attack? Y/N: ").lower()
			if action == "y":
				if self.player.defend():
					print("You dodged the hit!")
				else:
					print("Sorry, you got hit anyway!")
					self.player.wounded()
			else:
				self.player.wounded()
		else:
			print("You got lucky. {} isn't attacking this turn.".format(self.monster))

	def cleanup(self):
		if self.monster.hp <= 0:
			self.player.xp += self.monster.xp
			print("You've slayed the monster! Go kill the next one.")
			self.get_next_monster()

Game()