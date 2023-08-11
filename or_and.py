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
