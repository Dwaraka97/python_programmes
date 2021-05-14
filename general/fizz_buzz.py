number_of_rounds = int(input("Enter the number of rounds you want to play: "))

for i in range(1,number_of_rounds+1):
    if i % 3 == 0:
        if i % 5 ==0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)