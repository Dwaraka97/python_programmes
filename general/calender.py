import calendar

year = 2021
month = 4
print(calendar.month(year, month))

name = input("Enter first name and surname seperated with space: ")
firstname, surname = name.split()
print(f"{firstname}'s surname is {surname}")
numbers = [1, 2, 3, 4, 5]
str_nums = []
for number in numbers:
    str_nums.append(str(number))

print(" | ".join(str_nums))

word = input("Enter a word to find length: ")
print(len(word.strip()))

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

for quote in quotes:
    print(quote[1:-1])
for quote in quotes:
    print(quote.strip("'"))
