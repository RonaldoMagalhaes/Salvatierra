cars = {
	"make": "Ford",
	"model": "Fiesta",
	"mileage": 23000,
	"fuel_consumed": 460
}


def calculate_mpg(car):
	mpg = car["mileage"] / car["fuel_consumed"]
	return  mpg


mpg = calculate_mpg(cars)

print(f"{mpg} miles per galon.")