class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

class Linkedlist:

    def __init__(self):
        self.head = None
        self.numofnodes = 0

    def insert_start(self, data):

        self.numofnodes+=1
        new_node = Node(data)

        if not self.head:          #first node
            self.head = new_node
        else:
            new_node.nextnode = self.head   #new_node pointer will point to the previous one
            self.head = new_node            #the pointer of previous one will come to the new_node(the start of the list)
        
    def insert_end(self, data):
        #two pointers in this one

        self.numofnodes+=1
        new_node = Node(data)
        actual_node = self.head            

        while actual_node.nextnode is not None:       #goes till the end
            actual_node = actual_node.nextnode        

        actual_node.nextnode = new_node               #stops right before NULL and adds the new_node

    def size(self):
        print("\n\nsize of list: ")
        return self.numofnodes

    def traverse(self):
        print("\ntraverse function:")
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextnode
    
    def remove(self, data):
        if self.head is None:
            print("there is no list kya hatayega")
            return

        actual_node = self.head          #self.head pointer is always in the start of the list(insert func me)
        previous_node = None
        
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node                  #previous_node and actual pointer will go toether till actual==node.data
            actual_node = actual_node.nextnode
        
        if actual_node is None:
            print("search miss--> actual_node = None")
            return   #search miss

        if previous_node is None:
            print("previous_node is equal to None")
            self.head = actual_node.nextnode          #node.data was the first element of the list
            self.numofnodes-=1
        else:
            previous_node.nextnode = actual_node.nextnode     #this skips the node.data
            self.numofnodes-=1                                #previous_node is given the address of the next element from the node.data which skips it

ll = Linkedlist()
ll.insert_start(4)
ll.insert_start(10)
ll.insert_end(5)
ll.traverse()
