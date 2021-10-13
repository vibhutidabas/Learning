#Refer lecture 98. you made a note there(98 will help in the best way)  

import sys
import heapq

class Edge(object):

    def __init__(self, weight, startvertex, targetvertex):
        self.weight = weight                                        #weight of the vertex
        self.startvertex = startvertex
        self.targetvertex = targetvertex

class Node(object):                                                 #THIS MAINLY CREATES THE HEAP IN ORDER

    def __init__(self, name):                                       #dijkstra is greedy algo. it always visites the noe with min. distance 
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjlist = []
        self.mindist = sys.maxsize                                  #this means infinity(the max size in python)

    def __cmp__(self, othervertex):                                 #decides according to what we will select the min node(this does not work in python3 but it works in this) 
         return self.cmp(self.mindist, othervertex.mindist)         #as it is a heap it needs something to decide the order so cmp tells the order i.e. the min node 

    def __lt__(self, other):                                        #lt stands for "less than"
        selfPriority = self.mindist                                 #according to what we will define the order
        otherPriority = other.mindist                                     
        return selfPriority < otherPriority                         #how do we find which is smaller than the other one(this is how)

class Algo(object):                                                 #heaps are used in this algo. bec. it has O(1) complexity

    def calc_shortest_path(self, vertexlist, startvertex):
        
        q=[]                                                        #this is basically a heap(representation of heap in 1D)
        startvertex.mindist = 0                                     #this is the root node or the first node(A)
        heapq.heappush(q, startvertex)                              #pushed in the queue

        while q:                                                    #till the queue is not empty
            
            actualvertex = heapq.heappop(q)                         #return the node with the min. diastance(by using __cmp__ and __lt__)

            for edge in actualvertex.adjlist:                        
                u = edge.startvertex                                #(B)                       
                v = edge.targetvertex                               #(D, C, H)
                newdist = u.mindist + edge.weight                   #distane between them + weight of the node(for B and D(5+15))
                
                if newdist < v.mindist:                             #it means we have found a shorter path(any number < infinity(weight of the node))
                    v.predecessor = u                               #we update "v" in this by changing its predecessor and mindist
                    v.mindist = newdist 
                    heapq.heappush(q, v)                            #then we have to update the heap bec. we changed "v"

    def get_shortest_path(self, targetvertex):
        print("the shortest path to vertex is: ", targetvertex.mindist)

        node = targetvertex

        while node is not None:
            print("%s" % node.name)
            node = node.predecessor                                 #the predecessors were assigned in the previous function when the tree was being mapped

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n8 = Node("H")

e1 = Edge(5, n1, n2)
e2 = Edge(8, n1, n8)
e3 = Edge(9, n1, n5)
e4 = Edge(15, n2, n4)
e5 = Edge(12, n2, n3)
e6 = Edge(4, n2, n8)
e7 = Edge(7, n8, n3)
e8 = Edge(6, n8, n6)
e9 = Edge(5, n5, n8)
e10 = Edge(4, n5, n6)
e11 = Edge(20, n5, n7)
e12 = Edge(1, n6, n3)
e13 = Edge(13, n6, n7)
e14 = Edge(3, n3, n4)
e15 = Edge(11, n3, n7)
e16 = Edge(9, n4, n7)

n1.adjlist.append(e1)
n1.adjlist.append(e2)
n1.adjlist.append(e3)
n2.adjlist.append(e4)
n2.adjlist.append(e5)
n2.adjlist.append(e6)
n8.adjlist.append(e7)
n8.adjlist.append(e8)
n5.adjlist.append(e9)
n5.adjlist.append(e10)
n5.adjlist.append(e11)
n6.adjlist.append(e12)
n6.adjlist.append(e13)
n3.adjlist.append(e14)
n3.adjlist.append(e15)
n4.adjlist.append(e16)

vertexlist = (n1,n2,n3,n4,n5,n6,n7,n8)

a = Algo()
a.calc_shortest_path(vertexlist, n1)
a.get_shortest_path(n2)