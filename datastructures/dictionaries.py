friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob" : 22}

for name in friend_ages:
    print(friend_ages[name])
#slicing
t = (1,2,3,4,5,6)
print(t[4:2:-1])
print(t[::-1])
print(t[::2])

#negative slicing

print(t[-4:-1:-1]) #gives Empty list as u r slicing it in reverse order and the starting point is lower than ending point

print(t[-1:-4:-1])# gives the reverse list with negatice indexing
album = {
    "title" : "The Dark Side of the Moon",
    "artist" : "Pink Floyd",
    "release_year" : 1973,
    "tracks": (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}

for key, value in album.items():
    print(f"{key}, {value}")

del album['tracks']
del album['release_year']
album["date_of_release"] = "March 1st 1973"
album.update({"song1":"The Great Gig in the Sky", "song2" : "Brain Damage"})
for key, value in album.items():
    print(f"{key}, {value}")


print(album.get('tracks','Empty'))
