cars = {
	"make": "Ford",
	"model": "Fiesta",
	"mileage": 23000,
	"fuel_consumed": 460
}


def calculate_mpg(car):
	mpg = car["mileage"] / car["fuel_consumed"]
	name = f'{car["make"]} {car["model"]}'
	print(f"{name} does {mpg} miles per galon.")


calculate_mpg(cars)