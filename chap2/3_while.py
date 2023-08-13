is_learning = True

while is_learning:
	print("You're learning...")
	user_input = input("Are you still learning? ").lower()
	is_learning = user_input == "yes"
