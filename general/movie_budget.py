movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

sum = 0
for movie in movies:
    sum += movie[1]

average_budget = sum/len(movies)
count = 0
for movie in movies:
    if movie[1] > average_budget:
        print(f"{movie[0]} has {movie[1]-average_budget} than average budget")
        count +=1
print(f"{count} movies have more than average budget")
