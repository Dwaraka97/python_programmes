numbers = [1, 2, 3, 4, 5]
squares = []
[squares.append(number ** 2) for number in numbers]

print(squares)


movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

movie = {movie_key : movie_value.title() for movie_key,movie_value in movie.items()}

print(movie)