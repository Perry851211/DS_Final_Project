from Class import *
from Function2 import *

# initialize restaurant info
#set_seats = 5
set_seats = [3, 4, 5, 6, 7]
r_objs = [Restaurant() for i in range(5)]   # create Restaurant object list
restList = ["A", "B", "C", "D", "E"]
day_List = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_List = ["9", "10", "11", "12"]
item = 0

for k, r in enumerate(r_objs):
    r.restName = restList[item]
    r.book = {}
    for i in day_List:
        for j in time_List:
            r.book[(i, j)] = set_seats[k]
    item += 1
# input booking info
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
        # seat booking function
        seatBooking(b, r_objs, b_objs, b_name)

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
    print(reviewRank.array)

from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Restraurant Reservation!')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

# Creating frames
frame = LabelFrame(root, padx=40, pady=40)
frame.pack(padx=10, pady=10)

# Creating a Label Widget

myLabel_1 = Label(frame, text="Welcome to our Restraurant Reservation!").grid(row=0, column=0)
myLabel_2 = Label(frame, text="What do you want to do?").grid(row=1, column=0)

# Define Buttons
def button_click():
    return

##########################
### Define new windows ###
##########################

## 1. book seat ##
##################
def book_seat_wd():
  
    top = Toplevel()
    top.title('1. Book seat')
    top.geometry("300x650")
    
    frame2 = LabelFrame(top, padx=20, pady=20, text="Please enter your information")
    frame2.pack(padx=10, pady=10)

    myLabel_4 = Label(frame2, text="Name:")
    myLabel_4.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_5 = Label(frame2, text="Day:")
    myLabel_5.grid(row=1, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_6 = Label(frame2, text="Time:")
    myLabel_6.grid(row=2, column=0, ipadx=5, pady=5, sticky=W)
    # Name
    e = Entry(frame2, width=7, font=('Helvetica', 14))
    e.grid(row=0, column=1, ipadx=5, pady=5, sticky=E)
    # Day
    clicked1 = StringVar()
    clicked1.set(day_List[0])
    drop = OptionMenu(frame2, clicked1, *day_List)
    drop.grid(row=1, column=1, ipadx=5, pady=5, sticky=E)
    # Time
    clicked2 = StringVar()
    clicked2.set(time_List[0])
    drop = OptionMenu(frame2, clicked2, *time_List)
    drop.grid(row=2, column=1, ipadx=5, pady=5, sticky=E)
    
    ## record booking info ##
    #global b
    b = Booking()
    b_objs.append(b)    

    def show():
        # input booking information
        b.name = e.get()
        b_name.append(b.name)
        b.day = clicked1.get()
        b.time = clicked2.get()
        #print(b.name,b.day,b.time)
        #myLabel = Label(top, text=e.get()+clicked1.get()+clicked2.get()).pack()
        frame3 = LabelFrame(top, padx=10, pady=10, text="Reservation status")
        frame3.pack(padx=10, pady=10)
        
        for i, r in enumerate(r_objs):
            #capacity = str(r.book[(b.day, b.time)]) + "/" + str(set_seats)
            #print(r.restName, ": ", capacity)
            myLabel_7 = Label(frame3, text=r.restName+": ", fg="blue")
            myLabel_7.grid(row=i, column=0, ipadx=5, pady=5, sticky=W)
            myLabel_8 = Label(frame3, text=str(r.book[(b.day, b.time)]), fg="blue")
            myLabel_8.grid(row=i, column=1, ipadx=5, pady=5, sticky=W)
            myLabel_9 = Label(frame3, text="/    " + str(set_seats[i]), fg="blue")
            myLabel_9.grid(row=i, column=2, ipadx=5, pady=5, sticky=W)
            
        # list the top-k recommendation according to the reviews
        myLabel_7 = Label(frame3, text="Top 3", fg="red")
        myLabel_7.grid(row=0, column=3, ipadx=5, pady=5)
        myLabel_8 = Label(frame3, text="Recommendation:", fg="red")
        myLabel_8.grid(row=1, column=3, ipadx=5, pady=5)
        reviewRank.array.sort()
        print("Top_", str(top_k), " Recommendation:", sep = "")
        for i, r in enumerate(reviewRank.array):
            print(r[1], ": ", -r[0])    
            myLabel_8 = Label(frame3, text=r[1]+"   :   "+"%.1f"% -r[0], fg="red")
            myLabel_8.grid(row=i+2, column=3, ipadx=5, pady=5)
            #myLabel_9 = Label(frame3, text=": ")
            #myLabel_9.grid(row=i+1, column=4, ipadx=5, pady=5, sticky=E)
            #myLabel_10 = Label(frame3, text="%.1f"% -r[0])
            #myLabel_10.grid(row=i+1, column=5, ipadx=5, pady=5, sticky=E)
           
        # leave for the recommendation part
        # for name in restList:
        #     print(name, end = " ")
        # print()
        frame4 = LabelFrame(top, padx=10, pady=10, text="Please select")
        frame4.pack(padx=10, pady=10)
        
        myLabel_10 = Label(frame4, text="Restaurant:")
        myLabel_10.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
        myLabel_11 = Label(frame4, text="Number of people:")
        myLabel_11.grid(row=1, column=0, ipadx=5, pady=5, sticky=W)
        # Restaurant
        clicked3 = StringVar()
        clicked3.set(restList[0])
        drop = OptionMenu(frame4, clicked3, *restList)
        drop.grid(row=0, column=1, ipadx=5, pady=5, sticky=E)
        b.restName = clicked3.get()
        #print(b.restName)       
        
        # Number of people
        e2 = Entry(frame4, width=5, font=('Helvetica', 14))
        e2.grid(row=1, column=1, ipadx=5, pady=5, sticky=E)
        #print(e2.get())

        # seat booking function
        def seatBooking(b, r_objs, b_objs, b_name):   # b: Booking
            b.restName = clicked3.get()
            b.num = int(e2.get())
            #print(b.restName,b.num)
            for r in r_objs:
                if r.restName == b.restName:
                    if r.book[(b.day, b.time)] - b.num >= 0:
                        response = messagebox.askokcancel("This is my Popup!", "Submit?")
                        if response==1:
                            r.book[(b.day, b.time)] -= b.num
                            top.destroy()
                            #print("Booking Successful!")
                            #print(r.book[(b.day, b.time)])
                            return
                        else:
                            top.destroy()
                            return
            # else remove the booking name and history
            b_objs.remove(b)    # actually it can be removed
            b_name.remove(b.name)
            #print("Not enough seats!")
            messagebox.showinfo("This is my Popup!", "Not enough seats!")
            top.destroy()

        myButton2 = Button(top, text="Submit", command=lambda: seatBooking(b, r_objs, b_objs, b_name)).pack()

    myButton = Button(top, text="Show Selection", command=show).pack()

## 2. Cancel booking ##
#######################
def Cancel_booking_wd():
  
    top = Toplevel()
    top.title('2. Cancel booking')
    top.geometry("300x360")
    
    frame2 = LabelFrame(top, padx=20, pady=20, text="Please enter your information")
    frame2.pack(padx=10, pady=10)

    myLabel_4 = Label(frame2, text="Name:")
    myLabel_4.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_5 = Label(frame2, text="Day:")
    myLabel_5.grid(row=1, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_6 = Label(frame2, text="Time:")
    myLabel_6.grid(row=2, column=0, ipadx=5, pady=5, sticky=W)
    # Name
    e = Entry(frame2, width=7, font=('Helvetica', 14))
    e.grid(row=0, column=1, ipadx=5, pady=5, sticky=E)
    # Day
    clicked1 = StringVar()
    clicked1.set(day_List[0])
    drop = OptionMenu(frame2, clicked1, *day_List)
    drop.grid(row=1, column=1, ipadx=5, pady=5, sticky=E)
    # Time
    clicked2 = StringVar()
    clicked2.set(time_List[0])
    drop = OptionMenu(frame2, clicked2, *time_List)
    drop.grid(row=2, column=1, ipadx=5, pady=5, sticky=E)

    ## Cancel booking ##
    def exit():
        top.destroy()
    def show():
        frame3 = LabelFrame(top, padx=10, pady=10, text="Cancel booking")
        frame3.pack(padx=10, pady=10)
        #print(e.get(),clicked1.get(),clicked2.get())
        for b in b_objs:
            if b.name == e.get() and b.day == clicked1.get() and b.time == clicked2.get():
                # remove name in booking list and only remove one if there are two names the same
                b_name.remove(e.get())
                # remove booking object
                b_objs.remove(b)
                # remove restaurant record by matching the restaurant name
                for r in r_objs:
                    if r.restName == b.restName:
                        r.book[(b.day, b.time)] += b.num    
                #print("Cancellation Successful!")
                myLabel_7 = Label(frame3, text="Cancellation Successful!")
                myLabel_7.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
                Button(top, text="Exit", command=exit).pack()
                return
        #print("Cancellation Fail!")
        myLabel_7 = Label(frame3, text="Cancellation Fail!")
        myLabel_7.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
        Button(top, text="Exit", command=exit).pack()

    myButton = Button(top, text="Submit", command=show).pack()

## 3. Modify booking ##
#######################
def Modify_booking_wd():
  
    top = Toplevel()
    top.title('3. Modify booking')
    top.geometry("300x500")
    
    frame2 = LabelFrame(top, padx=20, pady=20, text="Please enter your information")
    frame2.pack(padx=10, pady=10)

    myLabel_4 = Label(frame2, text="Name:")
    myLabel_4.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_5 = Label(frame2, text="Day:")
    myLabel_5.grid(row=1, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_6 = Label(frame2, text="Time:")
    myLabel_6.grid(row=2, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_7 = Label(frame2, text="Restaurant:")
    myLabel_7.grid(row=3, column=0, ipadx=5, pady=5, sticky=W)
    
    # Name
    e = Entry(frame2, width=7, font=('Helvetica', 14))
    e.grid(row=0, column=1, ipadx=5, pady=5, sticky=E)
    # Day
    clicked1 = StringVar()
    clicked1.set(day_List[0])
    drop = OptionMenu(frame2, clicked1, *day_List)
    drop.grid(row=1, column=1, ipadx=5, pady=5, sticky=E)
    # Time
    clicked2 = StringVar()
    clicked2.set(time_List[0])
    drop = OptionMenu(frame2, clicked2, *time_List)
    drop.grid(row=2, column=1, ipadx=5, pady=5, sticky=E)
    # Restaurant
    clicked3 = StringVar()
    clicked3.set(restList[0])
    drop = OptionMenu(frame2, clicked3, *restList)
    drop.grid(row=3, column=1, ipadx=5, pady=5, sticky=E)
    b.restName = clicked3.get()

    ## Modify booking ##
    def show():
        frame3 = LabelFrame(top, padx=10, pady=10, text="Modify booking")
        frame3.pack(padx=10, pady=10)
        #print(e.get(),clicked1.get(),clicked2.get())
        if e.get() not in b_name:
            #print("No booking history!")
            messagebox.showinfo("This is my Popup!", "No booking history!")
            top.destroy()
            return

        check = False
        for b in b_objs:
            if b.name == e.get() and b.day == clicked1.get() and b.time == clicked2.get() and b.restName == clicked3.get():
                # modify booking object, we assume customer would only reduce the number
                #print(b.name, " ", b.day, " ", b.time, ":00 ", b.num)
                myLabel_7 = Label(frame3, text="Number of people:")
                myLabel_7.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
                myLabel_8 = Label(frame3, text="Enter the number:")
                myLabel_8.grid(row=1, column=0, ipadx=5, pady=5, sticky=W)
                myLabel_9 = Label(frame3, text=str(b.num))
                myLabel_9.grid(row=0, column=1, ipadx=5, pady=5, sticky=W)
                #num = input("Change the number of people:")
                e2 = Entry(frame3, width=5, font=('Helvetica', 14))
                e2.grid(row=1, column=1, ipadx=5, pady=5, sticky=W)
                check = True

        def modify_show():
            num = int(e2.get())
            response = messagebox.askokcancel("This is my Popup!", "Submit?")
            if response==1:
                for b in b_objs:
                    if b.name == e.get() and b.day == clicked1.get() and b.time == clicked2.get() and 0 < num <= b.num:
                        diff = b.num - num
                        b.num = num
                        # remove restaurant record by matching the restaurant name
                        for r in r_objs:
                            if r.restName == b.restName:
                                r.book[(b.day, b.time)] += diff
                                #print("Modification Successful!")
                                top.destroy()
                        return
                #print("Modification Fail!")
                messagebox.showinfo("This is my Popup!", "Modification Fail!")
                top.destroy()
            else:
                top.destroy()
        if check:
            myButton2 = Button(top, text="Submit", command=modify_show).pack()
        else:
            #print("No booking history!")
            messagebox.showinfo("This is my Popup!", "No booking history!")
            top.destroy()
    myButton = Button(top, text="Show Selection", command=show).pack()



## 4. Check status ##
#######################
def Check_status():
    
    top = Toplevel()
    top.title('4. Check status')
    top.geometry("300x400")
    
    frame2 = LabelFrame(top, padx=20, pady=20, text="Please enter your information")
    frame2.pack(padx=10, pady=10)

    myLabel_1 = Label(frame2, text="Name:")
    myLabel_1.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_5 = Label(frame2, text="Day:")
    myLabel_5.grid(row=1, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_6 = Label(frame2, text="Time:")
    myLabel_6.grid(row=2, column=0, ipadx=5, pady=5, sticky=W)
    # Name
    e = Entry(frame2, width=10, font=('Helvetica', 14))
    e.grid(row=0, column=1, ipadx=5, pady=5, sticky=W)
    # Day
    clicked1 = StringVar()
    clicked1.set(day_List[0])
    drop = OptionMenu(frame2, clicked1, *day_List)
    drop.grid(row=1, column=1, ipadx=5, pady=5, sticky=E)
    # Time
    clicked2 = StringVar()
    clicked2.set(time_List[0])
    drop = OptionMenu(frame2, clicked2, *time_List)
    drop.grid(row=2, column=1, ipadx=5, pady=5, sticky=E)

    # history booking
    def exit():
        top.destroy()
    def show():
        for b in b_objs:
            if b.name == e.get() and b.day == clicked1.get() and b.time == clicked2.get():
                #print("-", b.restName, " ", b.day, " ", b.time, b.num)
                frame3 = LabelFrame(top, padx=20, pady=20, text="history booking")
                frame3.pack(padx=10, pady=10)  
                myLabel_2 = Label(frame3, text=b.restName)
                myLabel_2 .grid(row=0, column=1, ipadx=5, pady=5, sticky=E)
                myLabel_3 = Label(frame3, text=b.num)
                myLabel_3.grid(row=3, column=1, ipadx=5, pady=5, sticky=E)
                myLabel_4 = Label(frame3, text="Restaurant:")
                myLabel_4 .grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
                myLabel_5 = Label(frame3, text="Number of people:")
                myLabel_5.grid(row=3, column=0, ipadx=5, pady=5, sticky=W)
                Button(top, text="Exit", command=exit).pack()
                return
        Label(top, text="                   ").pack()
        Label(top, text="No booking history!", bg="red").pack()
        Label(top, text="                   ").pack()
        Button(top, text="Exit", command=exit).pack()

    myButton = Button(top, text="Show Selection", command=show).pack()

## 5. Leave comment ##
#######################
def Leave_comment():

    top = Toplevel()
    top.title('5. Leave comment')
    top.geometry("300x300")
    
    frame2 = LabelFrame(top, padx=20, pady=20, text="Please enter your information")
    frame2.pack(padx=10, pady=10)

    myLabel_1 = Label(frame2, text="Name:")
    myLabel_1.grid(row=0, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_2 = Label(frame2, text="Restaurant:")
    myLabel_2.grid(row=1, column=0, ipadx=5, pady=5, sticky=W)
    myLabel_3 = Label(frame2, text="Point of review(1-5):")
    myLabel_3.grid(row=2, column=0, ipadx=5, pady=5, sticky=W)
    # Name
    e = Entry(frame2, width=7, font=('Helvetica', 14))
    e.grid(row=0, column=1, ipadx=5, pady=5, sticky=E)
    # Restaurant
    clicked1 = StringVar()
    clicked1.set(restList[0])
    drop = OptionMenu(frame2, clicked1, *restList)
    drop.grid(row=1, column=1, ipadx=5, pady=5, sticky=E)
    # Point of review(1-5):
    points = [i for i in range(1,6)]
    clicked2 = StringVar()
    clicked2.set(points[0])
    drop = OptionMenu(frame2, clicked2, *points)
    drop.grid(row=2, column=1, ipadx=5, pady=5, sticky=E)

    # recalculate the review point of the restaurant and top-k rank of restaurant recommendation
    def modify_show():
        print(clicked1.get(),clicked2.get())
        restName = clicked1.get()
        review = int(clicked2.get())
        response = messagebox.askokcancel("This is my Popup!", "Submit?")
        if response==1:
            global reviewRank
            reviewRank = recalculate(restName, review, top_k, r_objs)
            #print(reviewRank.array)
            top.destroy()
        else:
            top.destroy()

    myButton2 = Button(top, text="Submit", command=modify_show).pack()


button_1 = Button(frame, text="1. Book seat", padx=66, pady=10, command=book_seat_wd).grid(row=2, column=0)
button_2 = Button(frame, text="2. Cancel booking", padx=49, pady=10, command=Cancel_booking_wd).grid(row=3, column=0)
button_3 = Button(frame, text="3. Modify booking", padx=48, pady=10, command=Modify_booking_wd).grid(row=4, column=0)
button_4 = Button(frame, text="4. Check status", padx=59, pady=10, command=Check_status).grid(row=5, column=0)
button_5 = Button(frame, text="5. Leave comment", padx=49, pady=10, command=Leave_comment).grid(row=6, column=0)

root.mainloop()
