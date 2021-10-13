capacity = 10                                                                #the max number of items

class Heap:

    def __init__(self):
        self.heap = [0]*capacity                                             #creates an array
        self.heap_size = 0                                                   #the counting variable

    def insert(self, item):  #O(1)

        if capacity == self.heap_size:                                       #if the list is full
            return

        self.heap[self.heap_size] = item                                     #assigning the item on the number
        self.heap_size+=1

        self.fix_up(self.heap_size-1)

    def fix_up(self, index): #O(logN)

        parent_index = (index-1)//2                                          #parent_index is the parent of the index

        if index > 0 and self.heap[index] > self.heap[parent_index]:         #if an item is greater than the parent 
            self.swap(index, parent_index)                                   #the rules are violated then swap
            self.fix_up(parent_index)                                        #to check again

    def swap(self, index1, index2):                                          #simple swap

        self.heap[index2] , self.heap[index1] = self.heap[index1], self.heap[index2]

    def get_max(self):     #O(1)                                              #this is the peek method
        return self.heap[0]                                                   #bec. the root node should be the largest(rule)

    def poll(self):  #O(logN)                                                 #it returns max item + removes it from the heap
        max = self.get_max()

        self.swap(0, self.heap_size-1)
        self.heap_size-=1

        self.fix_down(0)                                                      #after removing heap[0] the tree should be fixed 
        return max                                                            #bc. the spot is empty

    def fix_down(self, index):

        index_left = (2*index)+1                                              #left child of node(i) is 2i+1
        index_right = (2*index)+2                                             #right child of the node(i) is 2i+2 

        largest = index                                                       #heap[index] should be the largest
        
        if index_left<self.heap_size and self.heap[index_left] > self.heap[index]:
            largest = index_left                                              #if index_left is larger than the index then change largest

        if index_right<self.heap_size and self.heap[index_right] > self.heap[largest]:
            largest = index_right                                             #if index_right is lareger than the index then change largest

        if index!= largest:                                                   #in the end swap then making sure they are not same
            self.swap(index, largest)
            self.fix_down(largest)

    def heap_sort(self):    #O(N*logN)
        size = self.heap_size                                                 #we change the size in poll() so we have to store it

        for i in range(0, size):
            max = self.poll()
            print(max)

h = Heap()

h.insert(10)
h.insert(8)
h.insert(12)
h.insert(20)
h.insert(-2)
h.insert(1)
h.insert(0)
h.insert(321)

h.heap_sort()