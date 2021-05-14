from operator import methodcaller

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(lambda number: number ** 3, numbers)

for number in cubed_numbers:
    print(number)

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]

stripped = map(methodcaller("strip"),humpty_dumpty)

print(*stripped, sep='\n')
