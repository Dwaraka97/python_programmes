def sum(a, b=3):
    return a + b


print(sum(a=2))


def multi_greet(*names,other):
    for name in names:
        print(f"Hello, {name}!")


multi_greet("Jose", other='phil')
