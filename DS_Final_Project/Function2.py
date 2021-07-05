from Class import * 

def seatBooking(b, r_objs, b_objs, b_name):   # b: Booking
    for r in r_objs:
        if r.restName == b.restName:
            if r.book[(b.day, b.time)] - b.num >= 0:
                r.book[(b.day, b.time)] -= b.num
                print("Booking Successful!")
                return
    # else remove the booking name and history
    b_objs.remove(b)    # actually it can be removed
    b_name.remove(b.name)
    print("Not enough seats!")

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
