numbers = [0, 1, 2, 3, 4]
doubles_nums = [n * 2 for n in numbers]

print(numbers)
print(doubles_nums)

print("*" * 80)

friends_ages = [22, 31, 35, 37]

age_str = [f"My friend is {x} years old." for x in friends_ages]
print(age_str)

print("*" * 80)

names = ["Rolf", "Bob", "Jen"]

names_lowerCase = [name.lower() for name in names]
print(names_lowerCase)  # ['rolf', 'bob', 'jen']
