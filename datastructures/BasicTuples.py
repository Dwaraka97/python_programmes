movies = [("Eternal Sunshine of the Spotless Mind", 2004, "1 Billion")]

user_movie=[]
user_movie = input("Enter movie name: ").split(",")
user_movie[1] = int(user_movie[1])
user_movie=tuple(user_movie)
print(f"movie name: {user_movie[0]} released in {user_movie[1]}")
movies.append(user_movie)
print(movies)
movies.pop(0)
print(movies)
