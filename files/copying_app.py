class Invite:

    """Take 3 friends names as input from user
        compare them with people names in people.txt file
        write the common friends name to nerarby_friends.txt file"""

    friends = input("Enter 3 friends names separated by comas: ").lower().split(",")
    if len(friends) < 3:
        print("Enter atleast 3 friends names!!!!!")
    else:
        with open("people.txt",'r') as people_file:
            people_nearby = [line.strip() for line in people_file.readlines()]
        people_nearby = [people.lower() for people in people_nearby]
        people_nearby_set = set(people_nearby)
        friends_set = set(friends)
        # get common names from people_nearby and friends sets
        friends_nearby_set = people_nearby_set.intersection(friends_set)

        with open("nearby_friends.txt",'w') as nearby_friends_file:
            for friend in friends_nearby_set:
                print(f"{friend} is nearby, Please invite over!")
                nearby_friends_file.write(f"{friend.title()}\n")


invite = Invite()

