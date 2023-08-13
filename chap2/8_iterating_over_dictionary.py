friends_age = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for key in friends_age:
	print("-" * 80)
	print(key)

for value in friends_age.values():
	print("-" * 80)
	print(value)

for k, v in friends_age.items():
	print("-" * 80)
	print(f"{k} => {v}")
