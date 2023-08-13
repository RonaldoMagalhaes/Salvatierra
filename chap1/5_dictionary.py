friends_age = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friends_age["Rolf"])

# adding
friends_age["Bob"] = 20
print(friends_age)  # {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}

# changing

friends_age["Rolf"] = 25
print(friends_age)  # {'Rolf': 25, 'Adam': 30, 'Anne': 27, 'Bob': 20}

friends = (
	{"name": "Rolf Smith", "age": 24},
	{"name": "Adam Wool", "age": 30},
	{"name": "Anne Pun", "age": 27},
)

print(friends[2]["name"])  # Anne Pun

amigos = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]

amigos_dict = dict(amigos)
print(amigos_dict)  # {'Rolf': 24, 'Adam': 30, 'Anne': 27}


