ages = [22, 35, 27, 21, 20]

odd_ages = [n for n in ages if n % 2 == 1]
print(ages)
print(odd_ages)

friends = ["Rolf", "ruth", "charlie", "jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

friends_party = friends_lower.intersection(guests_lower)
print(friends_party)

