import os
import sys

movies = []

MENU = """
####################################  MENU  ##########################################

			1 - Add Movie
			2 - Lista all movies
			3 - Find a movie by it's title
			4 - Quit

######################################################################################

Enter your option: """


def add():
	print()
	print("=" * 80)
	title = input("Enter the movie title: ")
	director = input("Enter the movie director: ")
	release_year = input("Enter the movie release year: ")

	movies.append({
		"title": title,
		"director": director,
		"release_year": release_year,
	})

	print()
	print("...  ✅  Movie was added to your list     ...")


def list_movie():
	for movie in movies:
		display(movie)


def display(movie):
	print()
	print("=" * 80)
	print(f"Movie title: {movie['title']}")
	print(f"Movie director: {movie['director']}")
	print(f"Movie release year: {movie['release_year']}")
	print("=" * 80)


def find_movie():
	search = input("Enter the movie title you are searching for: ").lower()

	for m in movies:
		if m["title"].lower() == search:
			display(m)
			break
	else:
		print(f"⛔️ Sorry, {search.title()} is not in your list")


def execute_code():
	run = True
	while run:
		op = int(input(MENU))
		if op == 4:
			print()
			print("...  🏁 Finishing your app     ...")
			run = False
			break
		elif op == 1:
			add()
		elif op == 2:
			list_movie()
		elif op == 3:
			find_movie()
		else:
			print("⛔️ Invalid entry. Please try again...")


execute_code()