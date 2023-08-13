import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

#lottery_numbers = {1, 3, 5, 7, 9, 11}

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

winner = 0
winner_name = ""
for p in players:
    name = p["name"]
    game = p["numbers"]
    match = len(lottery_numbers.intersection(p["numbers"]))
    if match > winner:
        winner = match
        winner_name = name

    print(f"{name} => score: {match}")

print("#"*80)

print(f"{winner_name} => scored: {winner}")
