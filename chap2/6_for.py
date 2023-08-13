friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
	print(friend)

print("-" * 80)

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for element in elements:
	print(element)

print("-" * 80)

for _ in elements:
	print("RVM")


print("-" * 80)


for index in range(10):
	print(index, end=", ")

print("-" * 80)


students = [
	{"name": "Rolf", "grade": 90},
	{"name": "Bob", "grade": 78},
	{"name": "Jen", "grade": 100},
	{"name": "Anne", "grade": 80},
]

for student in students:
	print("-" * 80)
	name = student["name"]
	grade = student["grade"]

	print(f"Student: {name} => Grade: {grade}")

