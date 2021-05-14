for x in range(2, 11, 3):
    print(x, end=" ")
    if x == 3:
        break
    else:
        x = x - 1
else:
    print("Error")
