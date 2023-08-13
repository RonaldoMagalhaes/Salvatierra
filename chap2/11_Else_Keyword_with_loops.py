cars = ["ok", "ok", "ok", "ok", "ok", "ok"]

for status in cars:
	if status == "faulty":
		print("stopping production...")
		break  # stop the loop
	print(f"This car is {status}.")
	print("Shipping new car to the customer")
else:
	print("All cars built successfully. No faulty cars.")
	# essa linha roda se nao encontrar algum erro ou break


