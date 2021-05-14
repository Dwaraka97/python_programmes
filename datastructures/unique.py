def unique():
    l = [1, 2, 3, 1, 2, 6, 4, 7, 6]
    print(l)
    a = []
    for i in l:
        if i not in a:
            a.append(i)

    print(a)
unique()