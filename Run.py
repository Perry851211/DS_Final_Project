from Class import *
from Function import *
    
# def toWaitingList(booking): # booking: Booking

# def showWaitingList():


# initialize restaurant info
set_seats = 5
r_objs = [Restaurant() for i in range(5)]   # create Restaurant object list
restList = ["A", "B", "C", "D", "E"]
day_List = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_List = ["9", "10", "11", "12"]
item = 0
for r in r_objs:
    r.restName = restList[item]
    r.book = {}
    for i in day_List:
        for j in time_List:
            r.book[(i, j)] = set_seats
    item += 1
# print(r.book)

b_objs = []     # create Booking object list
b_name = []
top_k = 3

##### input some booking info by text document
input_path = "input_1.txt"
with open(input_path, 'r', newline='') as file_in:
    f = file_in.read().splitlines()
    for lines in f:
        value_list = lines.split(' ')
        b = Booking()
        b_objs.append(b)    # record booking info
        # input booking information
        b.name = value_list[0]
        b_name.append(b.name)
        b.day = value_list[1]
        b.time = value_list[2]
        b.restName = value_list[3]
        b.num = int(value_list[4])

        for r in r_objs:
            if r.restName == b.restName:
                if r.book[(b.day, b.time)] - b.num >= 0:
                    r.book[(b.day, b.time)] -= b.num
                    break

##### input some review info by text document
input_path = "input_2.txt"
with open(input_path, 'r', newline='') as file_in:
    f = file_in.read().splitlines()
    for lines in f:
        value_list = lines.split(' ')
        name = value_list[0]
        restName = value_list[1]
        review = int(value_list[2])
        
        # recalculate the review point of the restaurant and top-k rank of restaurant recommendation
        reviewRank = recalculate(restName, review, top_k, r_objs)
    # print(reviewRank.array)


##### input booking info by user interface
while True:
    print("What do you want to do?")
    print("1. Book seat")
    print("2. Cancel booking")
    print("3. Modify booking")
    print("4. Check status")
    print("5. Leave comment")
    
    user_input = input()
    
    ### Case 1:
    if user_input == "1":
        b = Booking()
        b_objs.append(b)    # record booking info
        
        # input booking information
        b.name = input("Your_name:")
        b_name.append(b.name)
        b.day = input("Day(Monday-Friday):")
        while b.day not in day_List:
            print("Spelling error!")
            b.day = input("Day(Monday-Friday):")
        b.time = input("Time(9-12):")
        while b.time not in time_List:
            print("Input error!")
            b.time = input("Time(9-12):")
        # list the remain seats info of restaurant
        for r in r_objs:
            r.capacity = str(r.book[(b.day, b.time)]) + "/" + str(set_seats)
            print(r.restName, ": ", r.capacity)
        # list the top-k recommendation according to the reviews
        reviewRank.array.sort()
        print("Top_", str(top_k), " Recommendation:", sep = "")
        for i in reviewRank.array:
            print(i[1], ": ", -i[0])
        
        b.restName = input("Restaurant_name:")
        while b.restName not in restList:
            print("Can't find!")
            b.restName = input("Restaurant_name:")
        b.num = int(input("Number of people:"))

        # seat booking function
        seatBooking(b, r_objs, b_objs, b_name)
    
    ### Case 2 & Case 3:
    elif user_input == "2" or user_input == "3":
        name = input("Your_name:")
        if name not in b_name:
            print("No booking history!")
            continue

        # list history booking
        historyBooking(name, b_objs)

        # choose the history record to cancel or modify
        day = input("Day(Monday-Friday):")
        while day not in day_List:
            print("Spelling error!")
            day = input("Day(Monday-Friday):")    
        time = input("Time(9-12):")
        while time not in time_List:
            print("Input error!")
            time = input("Time(9-12):")
        
        if user_input == "2":
            # cancel booking function
            cancelBooking(name, day, time, r_objs, b_objs, b_name)
        
        if user_input == "3":
            # modify booking function
            modifyBooking(name, day, time, r_objs, b_objs)

    ### Case 4:
    elif user_input == "4":
        name = input("Your_name:")
        if name not in b_name:
            print("No booking history!")
            continue

        # list history booking function
        historyBooking(name, b_objs)

    ### Case 5:
    elif user_input == "5":
        name = input("Your_name:")
        print("The restaurant name you want to leave comment:")
        for r in restList:
            # can use a drop-down list
            print(r)
        restName = input()
        review = int(input("Your point of review(1-5):"))
        
        # recalculate the review point of the restaurant and top-k rank of restaurant recommendation
        reviewRank = recalculate(restName, review, top_k)

        ### Not sure whether can I modify class or global variable inside a non-class function without passing it as a parameter ???

        # print(reviewRank.array)
        
    else: 
        continue

    user_input = input("Continue y/n?")
    if user_input == "n":
        break







