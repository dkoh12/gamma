'''
Challenge: Create an iterator for a list of lists with the following methods:
boolean **hasNext**()
    return true if there is another element in the set
int **next**()
    return the value of the next element in the array
void **remove**()
    remove the last element returned by the iterator.
    That is, remove the element that the previous **next()** returned
    This method can be called only once per call to **next()**,
    otherwise an exception will be thrown.
Given:  [[4],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
Print:  1 2 3 4 5 6 7 8 9 10
'''

class arrayIter:
    def __init__(self, lst):
        self.array = lst
        self.i = -1
        self.j = -1
        self.prev_i = 0
        self.prev_j = 0

    def isEmpty(self):
        return (len(self.array[self.i]) == 0)

    def incrementPointer(self):
        self.prev_i = self.i
        self.prev_j = self.j
        while (self.i < len(self.array) - 1):
            if (self.j < len(self.array[self.i]) - 1):
                self.j += 1
            else:
                self.j = 0
                self.i += 1
            if (self.isEmpty() == False):
                return

    def hasNext(self):
        self.incrementPointer()
        if (self.i < len(self.array) - 1):
            self.i = self.prev_i
            self.j = self.prev_j
            return True
        else:
            return False

    def next(self):
        if (self.hasNext()):
            self.incrementPointer()
            return self.array[self.i][self.j]
        else:
            print "ERROR! No next value"
            return None

    def remove(self):
        if (self.i == -1 and self.j == -1):
            print "ERROR"
        else:
            del self.array[self.i][self.j]
            self.j -= 1


def printElements(lst):
    obj = arrayIter(lst)
    while (obj.hasNext()):
        print obj.next()


a = [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
printElements(a)
obj = arrayIter(a)
print obj.next()
print "before:", obj.array
obj.remove()
print "after:", obj.array