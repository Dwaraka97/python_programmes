import random
user_guess = int(input("Guess and enter a number between 1 and 100 : "))

number = random.randint(0,9) * 10 + random.randint(0,9)
chances = 5

while chances > 1:
    if (user_guess > number) and (user_guess - number)>10:
        print("Your guess is too high")
        chances -= 1
    elif (user_guess < number) and (number - user_guess)>10:
        print("Your guess is too low")
        chances -= 1
    elif (user_guess < number) and (number - user_guess) < 10:
        print("Your guess is low")
        chances -= 1
    elif (user_guess > number) and (user_guess - number) < 10:
        print("Your guess is high")
        chances -= 1
    elif user_guess == number:
        print("You have got the number right!!!")
        break
    user_guess = int(input(f"{chances} chances left: "))
else:
    print("All chances expired u didn't find the number better luck next tym!!!!")
