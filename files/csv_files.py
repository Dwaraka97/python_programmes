with open("csv_data.csv",'r') as csv_file:
    contents = csv_file.readlines()
irises = []
for row in contents[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

    irises.append({
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    })

with open('iris.csv','a') as iris_csv:
    for iris in irises:
        iris_csv.write(','.join(iris.values())+"\n")
