for n in range(1,11):
	for x in range(2, n):
		if n % x == 0:
			print(f"{n} is not a prime number")
			break
	else:
		print(f"{n} is a prime number")
