file=open('myfile.txt', 'w')
file.write("This is the write command\nIt allows us to write in a particular file")
file.close()
file=open('myfile.txt')
l= file.read()
print(l)
print(len(l.split()))
print(len(l))
print(len(l.splitlines()))
