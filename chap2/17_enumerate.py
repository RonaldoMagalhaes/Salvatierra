friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends):
	print(counter, friend)

print("*" * 80)

print(list(enumerate(friends)))  # [(0, 'Rolf'), (1, 'John'), (2, 'Anna')]
