age = 30
print(age)
print(30)

age = 40
print(age)

friend_age = 23
print(friend_age)

countries_visited = 90
print(countries_visited)

PI = 3.14159

print(PI)

RADIANS_TO_DEGREES = 180 / PI

print(RADIANS_TO_DEGREES)

print("*" * 50)
# numbers

float_division = 12 / 3
print(float_division)  # 4.0

integer_division = 12 // 3  # 4
print(integer_division)

print(8 // 3)  # 2  remove everything from the decimal place

print("*" * 50)
# remainder - modulus  %

remainder = 5 % 3  # 2
print(remainder)

print("*" * 50)
###############  strings  ##########################

my_string = "Hello world"

print(my_string)

string_with_quotes = "Hello It´s me"
print(string_with_quotes)

print("*" * 50)

multiline = """Hello, world.

My name is Jose. Welcome to my program

"""

print(multiline)
print("*" * 50)

name = "Jose"
greeting = "Hello ," + name
print(greeting)

age = 34
# print("You are " + age) error

print("You are " + str(age))

print("*" * 50)

# f string

age = 44
print(f"You are {age} years old.")

print("*" * 50)
######## INPUT  #####################

my_name = "Jose"
your_name = input("Enter yout name: ")

print(f"Hello {your_name}. My name is {my_name}.")

print("*" * 50)
print()
age = int(input("Enter your age: "))
months = age * 12

print(f"You have lived for {months} months.")