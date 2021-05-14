N = input("Enter an odd number: ")
N = int(N)
M = N*3
i = 1
count = 0
m = (M - 3) // 2

while i <= N // 2:
    print("-" * m, end="")
    print(".|." * (i + count), end="")
    print("-" * m)
    count = count + 1
    i = i + 1
    m = m - 3

welcome = (M - 7) // 2
print('-' * welcome + 'WELCOME' + '-' * welcome)

while i > 1:
    m = m + 3
    i = i - 1
    count = count - 1
    print("-" * m, end="")
    print(".|." * (i + count), end="")
    print("-" * m)