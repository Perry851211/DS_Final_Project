from Class import * 

def seatBooking(b, r_objs, b_objs, b_name):   # b: Booking
    for r in r_objs:
        if r.restName == b.restName:
            if r.book[(b.day, b.time)] - b.num >= 0:
                r.book[(b.day, b.time)] -= b.num
                print("Booking Successful!")
                return
    # else remove the booking name and history
    b_objs.remove(b)    # actually the object can be removed
    b_name.remove(b.name)
    print("Not enough seats!")

def cancelBooking(name, day, time, r_objs, b_objs, b_name):
    for b in b_objs:
        if b.name == name and b.day == day and b.time == time:
            # remove name in booking list and only remove one if there are two names the same
            b_name.remove(name)
            # remove booking object
            b_objs.remove(b)
            # remove restaurant record by matching the restaurant name
            for r in r_objs:
                if r.restName == b.restName:
                    r.book[(b.day, b.time)] += b.num    
            print("Cancellation Successful!")
            return
    print("Cancellation Fail!")

def modifyBooking(name, day, time, r_objs, b_objs):
    for b in b_objs:
        if b.name == name and b.day == day and b.time == time:
            # modify booking object, we assume customer would only reduce the number
            print(b.name, " ", b.day, " ", b.time, ":00 ", b.num)
            num = input("Change the number of people:")
            diff = num - b.num
            b.num = num
            # remove restaurant record by matching the restaurant name
            for r in r_objs:
                if r.restName == b.restName:
                    r.book[(b.day, b.time)] += diff    
            print("Modification Successful!")
            return
    print("Modification Fail!")

def historyBooking(name, b_objs):
    print("Booking history:")
    for b in b_objs:
        if b.name == name:
            print("-", b.restName, " ", b.day, " ", b.time, ":00 ", b.num)

def recalculate(restName, review, top_k, r_objs):
    reviewRank = MaxHeap()
    for r in r_objs:
        if r.restName == restName:
            r.reviewNum += 1
            # index = reviewRank.getPos([r.review, r.restName])   # get the position to update the review 
            r.review = (r.review*(r.reviewNum-1) - review) / r.reviewNum    # claculate the review as negative to use the MaxHeap
        if len(reviewRank.array) < top_k:
            reviewRank.insert([r.review, r.restName])
        else:   # if more than or equal to top_k elements
            if reviewRank.array[0][0] > r.review:
                reviewRank.array[0] = [r.review, r.restName]
                reviewRank.maxHeapify(0)
    return reviewRank