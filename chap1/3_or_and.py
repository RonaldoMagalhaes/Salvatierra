age = 25

result = age > 18 and age < 65
print(result)

# Truthy and Falsy

bool(0)  # False
bool(13)  # True

bool("")  # Falsy
bool("Hello")  # True

bool([])  # Falsy
bool([1, 2, 3])  # True


default_age = 30
age = 0


user_age = age or default_age
print(user_age) # 30

default_greeting = "there"
name = input("Enter your name: (optional) ")

user_name = name or default_greeting
print(f"Hello {user_name}!")

