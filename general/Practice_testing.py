a = "abc"
b = "abc"
print(id(a))
print(id(b))
print(a is b)

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers.append(5)
print(numbers == new_numbers)
print(numbers is new_numbers)



employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for employee in employees:
    total_pay = employee[1] * employee[2]
    print("{} has to be paid {}$ at the end of the week.".format(employee[0],total_pay))

sum=0
for employee in employees:
    sum=employee[2]+sum
avg = sum/len(employees)
for employee in employees:
    if employee[2] > avg:
        print(f"\n{employee} gets {employee[2]-avg}$ more than average salary")


