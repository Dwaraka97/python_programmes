def add(*items):
    print(sum(items))


add(1, 2, 3, 4, 5, 2, 3, 6, 7, 4, 1, 45, 6)


def hybrid(*names, **student):
    print(f"The values provided as positional arguments are: {names}", end=' ')
    # method 2
    for name in names:
        print(f"{name}", end=' ')

    print(f"\nThe values provided by keyword arguments are: {student}", end=' ')
    # method 2
    print("id of {name} is {id}".format(**student))
    for key,value in student.items():
        print(f"{key}: {value}")


students = {"id": 1312,"name": "Dwarak"}
hybrid("Dwarak", "Jose", "Rolf", "Smith",**students)


hybrid("Dwarak", "Jose", "Rolf", "Smith",[1,2,3],id=132,name='abc')


def keyword(**country):
    print("{name} has {population} population, {name}'s capital is {capital} and currency is {currency}".format(**country))


country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

keyword(**country)

print(*range(1,28),sep=',')
#print(*range(1,28),sep='\n')