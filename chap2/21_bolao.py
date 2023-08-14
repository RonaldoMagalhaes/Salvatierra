players = [
	{"name": "Ronaldo", "numbers": {19, 37, 31, 45, 39, 60}},
	{"name": "Ronaldo", "numbers": {35, 40, 10, 60, 7, 17}},
	{"name": "Ronaldo", "numbers": {50, 24, 58, 36, 41, 22}},
	{"name": "Ronaldo", "numbers": {39, 20, 4, 21, 31, 12}},

	{"name": "Jose Antonio", "numbers": {1, 3, 25, 33, 45, 51}},
	{"name": "Jose Antonio", "numbers": {5, 8, 16, 34, 46, 58}},
	{"name": "Jose Antonio", "numbers": {12, 16, 22, 34, 36, 51}},
	{"name": "Jose Antonio", "numbers": {6, 16, 26, 36, 46, 56}},

	{"name": "Diego", "numbers": {22, 17, 30, 8, 27, 10}},
	{"name": "Diego", "numbers": {7, 10, 13, 21, 37, 59}},
	{"name": "Diego", "numbers": {1, 7, 19, 30, 37, 55}},
	{"name": "Diego", "numbers": {8, 13, 16, 17, 22, 23}},

	{"name": "Mineiro", "numbers": {3, 11, 21, 22, 47, 50}},
	{"name": "Mineiro", "numbers": {23, 28, 29, 38, 42, 53}},
	{"name": "Mineiro", "numbers": {13, 19, 20, 44, 45, 51}},
	{"name": "Mineiro", "numbers": {2, 12, 24, 25, 32, 40}},

	{"name": "Charles", "numbers": {8, 12, 27, 42, 50, 55}},
	{"name": "Charles", "numbers": {7, 16, 30, 38, 48, 60}},
	{"name": "Charles", "numbers": {10, 22, 41, 53, 59, 19}},
	{"name": "Charles", "numbers": {3, 11, 23, 32, 47, 51}},

]

loterry_number = {4, 6, 13, 21, 26, 28}

total_score = 0
winner = ""
for p in players:
	name = p["name"]
	numbers = p["numbers"]
	matches = len(numbers.intersection(loterry_number))
	if matches > total_score:
		total_score = matches
		winner = name

	print(f"{name} => sored: {matches}")

print("#" * 80)
print(f"Winner : {winner} => Matches: {total_score}")
