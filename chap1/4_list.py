friends = ["Rolf", "Bob", "Anne"]

print(friends[0])
print(friends[1])
print(friends[2])

print(len(friends))

friends2 = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]

print(friends2)
print(friends2[2][0])

# add to a list  - use append

friends.append("Jen")
print(friends)

# remove from a list - use remove

friends.remove("Rolf")
print(friends)