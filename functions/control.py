def control():
    time=input("Enter time")
    time=int(time)
    if(time>=6 and time < 7):
        print("Go for a Morning Walk")
    elif(time >= 7 and time < 8):
        print("Take a shower")
    elif(time >= 8 and time < 9):
        print("Have breakfast")
    elif(time >=10 and time < 11):
        print("Go to office")
    elif(time >= 13 and time < 14):
        print("Have lunch")
    elif(time>= 18 and time < 19):
        print("go home")
    elif(time>= 21 and time <22):
        print("go to sleep")
    else:
        print("enter valid time")


control()
