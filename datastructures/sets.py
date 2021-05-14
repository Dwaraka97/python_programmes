s = set()
s1={"Dwaraka", "python", "master"}
s2 = set()
print(type(s2))
s2.add(1)
s2.update({"Dwaraka","Ravi", "sagar"})
print(s2.symmetric_difference(s1))
print(s2.difference(s1))
print(s1.difference(s2))
print(s2.union(s1))

print(s2.intersection(s1))

for i in range(0,99):
    s.add(i)

user_input = int(input("Enter a number: "))
if user_input in s:
    print(f"{user_input} is in the set")
else:
    print(f"{user_input} is out of set range")
