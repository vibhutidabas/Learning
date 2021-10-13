import sys

class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjlist = []
        self.predecessor = None
        self.mindist = sys.maxsize

class Edge(object):

    def __init__(self, weight, startvertex, targetvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex

class BellmanFord(object):
    
    HAS_CYCLE = False

    def calc_shortest_path(self, vertexlist, edgelist, startvertex):

        startvertex.mindist = 0

        for i in range(0, len(vertexlist)-1):                                           #unlike dijkstra bellman notes every single vertex and edge repeatedly
            for e in edgelist:                                                          #it is robust but helps with the negative cycles thats it

                u = e.startvertex
                v = e.targetvertex

                newdist = u.mindist + e.weight

                if newdist < v.mindist:
                    v.mindist = newdist
                    v.predecessor = u

        for e in edgelist:
            if self.hascycle(e):                                                        #if it is a neg. cycle, the pointer will come back(as it is a cycle) 
                print("negative cycle found...")                                        #the previous mindist value of a vertex will be greater than the new one
                BellmanFord.HAS_CYCLE = True
                return

    def hascycle(self, edge):
        
        if (edge.startvertex.mindist + edge.weight) < edge.targetvertex.mindist:        #the new one should be less than the old mindist then only it will be a negative cycle
            return True
        else:
            return False

    def shortest_path(self, targetvertex):
        
        if not BellmanFord.HAS_CYCLE:
            print("shortest path exists with value: ", targetvertex.mindist)

            node = targetvertex

            while node is not None:
                print("%s" % node.name)
                node = node.predecessor

        else:
            print("negative cycle detected...")

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
edgelist = (e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16)

b = BellmanFord()
b.calc_shortest_path(vertexlist, edgelist, n1)
b.shortest_path(n7)