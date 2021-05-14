# we can also provide the complete path as below if we want to
my_file = open('C:/Users/dchittepu/PycharmProjects/Python/files/data.txt','r')
# read mode can access and read the file but can't modify it
file_content = my_file.read()
my_file.close()
print(file_content)

user_input = input("Enter a name: ")
# . means current directory
# my_file = open('./data.txt','w')
#
# my_file.write(user_input)
# my_file.close()

with open("data.txt",'a') as my_file:
    my_file.write(f"{user_input} is the owner of the file\n")
