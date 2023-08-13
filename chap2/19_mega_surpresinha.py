import random


def game_surprise():
	game = set(random.sample(list(range(61)), 6))
	return game


for n in range(10):
	print("-"*80)
	print(game_surprise())



