base_10 = 231

print(f"This is the number in binary: {base_10 :b}")

print(f"This is the number in octal: {base_10 :o}")

print(f"This is the number in hexadecimal: {base_10 :x}")

print(f"This is the number in uppercase hexadecimal: {base_10 :X}")

base_16 = int("E7", base=16)

print(f"This is the number in decimal: {base_16 :d}")


print(format(12, "02x"))


x = 4863.4345091          # example float to format

print(f"{x:.6}")          # f-string version
print("{:.6}".format(x))

x = 4863.4343091

print(f"{x:.3f}")



number_of_files = 3
number_digits = int(input("How many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
	print("image{:0{}}.png".format(file_number, number_digits))


a = int("E7", base=16)
print(a)


example_tuple = 1, 2, 3

print(type(example_tuple))
print(format(example_tuple))



numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]


numbers = [1, 2, 3, 4]
numbers.append(5)

print(new_numbers is numbers)