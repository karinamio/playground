import random

class Combat:
	def_limit = 6
	atk_limit = 6

	def defend(self):
		roll = random.randint(1, self.def_limit)
		return roll > 4

	def attack(self):
		roll = random.randint(1, self.atk_limit)
		return roll > 4