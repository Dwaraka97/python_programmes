def parent(a,b):
    def child(string):
        print(string+"\n")
        print(a*b)
    return child
x=5
callChild = parent(2,x)
callChild("Hello there!")

print(type(callChild.__closure__))
print(len(callChild.__closure__))
print([cell for cell in callChild.__closure__])
del(x)
callChild("x deleted")
print([cell.cell_contents for cell in callChild.__closure__])
# t=(10,9,8,7)
# print(type(t))
# print([t[i] for i in range(len(t))])