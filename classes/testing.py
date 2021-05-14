# Define a Movie class that has two properties: name and director
class Movie:
    def __init__(self, movie_name, director_name):
        self.movie = movie_name
        self.director = director_name

        movies = {'name': self.movie, 'director': self.director}


# You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski')
print(my_movie)

st = 'python programming'
for i in range(len(st)):
    end_value = '_'
    if st[i] == ' ':
        end_value = ''
    if i % 1 == 0:
        print(st[i].upper(), end=end_value)
    else:
        print(st[i], end=end_value)
