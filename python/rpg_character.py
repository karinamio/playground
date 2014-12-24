from random
from rpg_combat import Combat

# base class for players
class Character(Combat):
	xp = 0
	atk_limit = 10
	starting_hp = 10

	# constructor method
	def __init__(self, **kwargs):
		self.name = input("Enter a name for your character: ")
		self.weapon = self.get_weapon()
		self.hp = self.starting_hp
		for key, value in kwargs.items():
			setattr(self, key, value)

	# pretty print method
	def __str__(self):
		return '{} [ HP: {}, XP: {} ]'.format(self.name, self.hp, self.xp)

	def attack(self):
		roll = random.randint(1, self.atk_limit)
		if self.weapon == "sword":
			roll += 1
		elif self.weapon == "axe":
			roll += 2
		return roll > 4

	def get_weapon(self):
		weapon_choice = input("Choose a weapon from the following list: ([s]word, [a]xe, [b]ow): ").lower()
		if weapon_choice in 'sab':
			if weapon_choice == 's':
				return 'sword'
			if weapon_choice == 'a':
				return 'axe'
			if weapon_choice == 'bow':
				return 'bow'
		else:
			print("That's not on the list. Try again")
			return self.get_weapon()

	def wounded(self):
		self.hp -= 1
		print("You've been hit for 1 point!")

	def rest(self):
		if self.hp < self.starting_hp:
			self.hp += 1
			print("You gained 1 HP!")
		else:
			print("Sorry, your HP is already maxed out.")

	def level_up(self):
		print("Nice, you leveled up!")
		return self.xp >= 5