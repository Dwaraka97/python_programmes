def killer_fun():
    l=[i+1 for i in range(0,100)]
    while len(l) > 1:
        killer = l.pop(0)
        l.append(killer)
        del l[0]
    print(l)
killer_fun()