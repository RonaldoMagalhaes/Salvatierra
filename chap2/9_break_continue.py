cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
	if status == "faulty":
		print("stopping production...")
		break  # stop the loop
	print(f"This car is {status}.")
	print("Shipping new car to the customer")

print("#" * 80)

# continue

for status in cars:
	if status == "faulty":
		print("Found faulty car, skipping...")
		continue  # continue the loop  IT JUST GOES TO NEXT ONE TO THE TOP OF THE LOOP
	print(f"This car is {status}.")
	print("Shipping new car to the customer")
