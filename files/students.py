import csv

student_data = [{'Id': 3500129, 'name': 'Dwarakanath'}, {'Id': 3500121, 'name': 'Srikanth'},
                {'Id': 3500148, 'name': 'Ram charan'}, {'Id': 3500124, 'name': 'Ravi kiran'},
                {'Id': 3500486, 'name': 'Rohit'}]


def write(students):
    with open("./student.csv", 'w') as file:
        file.write("Id,name\n")
        for student in students:
            file.write(f"{student['Id']},{student['name']}\n")


def read():
    with open("./student.csv") as file:
        lines = file.readlines()
        for line in lines[1:]:
            stripped_line = line.strip().split(",")
            print(f"Student Id: {stripped_line[0]}  Student Name: {stripped_line[1]}")


def dict_write(students):
    with open("./student.csv", 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Id','name'])
        writer.writeheader()
        writer.writerows(students)
        # for student in students:
        #     file.write(f"{student['Id']},{student['name']}\n")


def dict_read():
    with open("./student.csv") as file:
        lines = csv.DictReader(file)
        for line in lines:
            # stripped_line = line.strip().split(",")
            print(f"Student Id: {line['Id']}  Student Name: {line['name']}")


dict_write(student_data)
dict_read()
