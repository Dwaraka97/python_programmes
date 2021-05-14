zipped = [("John", 26), ("Anne", 31), ("Peter", 29)]
names, ages = zip(*zipped)
tup = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, number,(department,subject)=tup
print(f"{name} roll no {number} in {department} studying subject {subject}")
print(names)
print(ages)


from itertools import zip_longest

l_1 = [1, 2, 3]
l_2 = (1, 2)


combined = list(zip(l_1, l_2))

print(combined)

combined = list(zip_longest(l_1, l_2, fillvalue="_"))

print(combined)
movie_titles = [
	"Forrest Gump",
	"Howl's Moving Castle",
	"No Country for Old Men"
]

movie_directors = [
	"Robert Zemeckis",
	"Hayao Miyazaki",
	"Joel and Ethan Coen"
]

movies = list(zip(movie_titles, movie_directors))

for movie,(title,director) in enumerate(movies,start=1):
    print(f"{movie}. {title} is directed by {director}")