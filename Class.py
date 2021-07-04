class Restaurant:
    def __init__(self):
        self.restName = ""
        self.book = None    # day, time, SeatsNum
        self.capacity = ""
        self.review = 0     # the review that customer gave
        self.reviewNum = 0

class Booking:
    def __init__(self):
        self.name = ""
        self.restName = ""
        self.day = ""
        self.time = ""
        self.num = 0
        
class MaxHeap: #Please store and implement MaxHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getPos(self, lists):
        # original way already uses O(N)...
        for i in range(self.size):
            if self.array[i][1] == lists[1]:
                return i
    def getSize(self):
        return self.size
    def parent(self, pos):
        return (pos-1)//2
    def swap(self, fpos, spos):
        self.array[fpos], self.array[spos] = self.array[spos], self.array[fpos]
    def insert(self, lists): #insert new list item
        self.array.append(lists)
        self.size += 1
        current = self.size-1
        if self.size == 1:
            return
        # adjust the maxheap if needed
        while self.array[current][0] > self.array[self.parent(current)][0] and current != 0:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def isLeaf(self, pos):
        if pos >= self.size//2 and pos <= self.size-1:
            return True
        if self.size == 0 or self.size == 1:
            return True
        return False
    
    def maxHeapify(self, pos):

        ### Case 1: pos is leaf only compare with root
        if self.isLeaf(pos):
            while self.array[pos][0] > self.array[self.parent(pos)][0] and pos != 0:
                self.swap(pos, self.parent(pos))
                pos = self.parent(pos)

        ### Case 2: pos is root only compare with leaf
        elif pos == 0:
            if len(self.array)-1 >= 2*pos + 2:  # Check if both child exist to avoid nonexist index of list 
                if (self.array[pos][0] < self.array[2*pos + 1][0] or
                    self.array[pos][0] < self.array[2*pos + 2][0]):

                    # Swap with the left child and heapify the left child
                    if self.array[2*pos + 1][0] > self.array[2*pos + 2][0]:
                        self.swap(pos, 2*pos + 1)
                        self.maxHeapify(2*pos + 1)
    
                    # Swap with the right child and heapify the right child
                    else:
                        self.swap(pos, 2*pos + 2)
                        self.maxHeapify(2*pos + 2)
            else:
                # Only left child
                if self.array[pos][0] < self.array[2*pos + 1][0]:
                    # Swap with the left child
                    self.swap(pos, 2*pos + 1)

        # Case 3: pos is not roof or leaf
        else:
            # Compare with parent
            if self.array[pos][0] > self.array[self.parent(pos)][0]:
                while self.array[pos][0] > self.array[self.parent(pos)][0] and pos != 0:
                    self.swap(pos, self.parent(pos))
                    pos = self.parent(pos)

            # Compare with children
            else:
                if len(self.array)-1 >= 2*pos + 2:  # Check if both child exist to avoid nonexist index of list 
                    if (self.array[pos][0] < self.array[2*pos + 1][0] or
                        self.array[pos][0] < self.array[2*pos + 2][0]):

                        # Swap with the left child and heapify the left child
                        if self.array[2*pos + 1][0] > self.array[2*pos + 2][0]:
                            self.swap(pos, 2*pos + 1)
                            self.maxHeapify(2*pos + 1)
        
                        # Swap with the right child and heapify the right child
                        else:
                            self.swap(pos, 2*pos + 2)
                            self.maxHeapify(2*pos + 2)
                else:
                    # Only left child
                    if self.array[pos][0] < self.array[2*pos + 1][0]:
                        # Swap with the left child
                        self.swap(pos, 2*pos + 1)                

    def peek(self):    #Find Maximum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMax(self):   #Find Maximum item
        if self.size == 0:
            return
        self.array[0] = self.array[self.size-1]
        self.size -= 1
        item = self.array.pop()
        self.maxHeapify(0)
        return item

    def showMaxHeap(self):   #Show MaxHeap with array
        return self.array
