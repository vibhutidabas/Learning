class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.node = None

class Node(object):
    
    def __init__(self, height, nodeid, parentnode):
        self.parentnode = parentnode
        self.height = height
        self.nodeid = nodeid

class Edge(object):

    def __init__(self, weight, startvertex, targetvertex):         #weight, start and target vertex of edges
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex

    def __cmp__(self, otheredge):
        return self.cmp(self.weight, otheredge.weight)             #comparing edges by their weight

    def __lt__(self, other):
        selfpriority = self.weight
        otherpriority = other.weight
        return selfpriority < otherpriority

class Disjoint(object):

    def __init__(self, vertexlist):                                #no. of rootnode == no. of nodes == no. of vertexs
        self.vertexlist = vertexlist
        self.rootnodes = []                                        #there can be two trees therefore, two roots are possible
        self.nodecount = 0                                         #no. of nodes
        self.setcount = 0                                          #no. of sets
        self.makesets(vertexlist)                                  #in the start we will make as many sets as vertexs

    def find(self, node):
        
        currentnode = node

        while currentnode.parentnode is not None:                  #parent of rootnode is None
            currentnode = currentnode.parentnode                   #will get out of the loop when currentnode == rootnode 

        root = currentnode                                         #told ya
        currentnode = node                                         #again currentnode == node(given)

        while currentnode is not root:                             #loop is compressing the tree by connecting all the nodes to rootnode directly
            temp = currentnode.parentnode
            currentnode.parentnode = root
            currentnode = temp

        return root.nodeid

    def merge(self, node1, node2):
        
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:                                       #they are in the same set
            return
        
        root1 = self.rootnodes[index1]
        root2 = self.rootnodes[index2]

        if root1.height < root2.height:                            #if tree of root1 is smaller than root2 then root1's parent will be root2
            root1.parentnode = root2

        elif root1.height > root2.height:                          #if tree of root2 is smaller than root1 then root2's parent will be root1
            root2.parentnode = root1

        else:                                                      #they both are of equal size so it doesnt't matter which connects to which
            root2.parentnode = root1
            root1.height+=1                                        #root1 ki height badhi kyonki root1 se connect hua root2 ki bhi ho sakti hai

    def makesets(self, vertexlist):
       
        for v in vertexlist:
            self.makeset(v)

    def makeset(self, vertex):

        node = Node(0, len(self.rootnodes), None)                  #creating a rootnode (nodeid = len of node and parentnode = none)
        vertex.node = node                                         #making node vertex's parent
        self.rootnodes.append(node)                                #appending the node in rootnodes list
        self.setcount+=1
        self.nodecount+=1

class Kruskal(object):

    def spanningtree(self, vertexlist, edgelist):

        d = Disjoint(vertexlist)                                   #makes every vertex a disjoint
        spanningtrees = []

        edgelist.sort()                                            #sorts the edgelist (helps in creating the tree)

        for e in edgelist:

            u = e.startvertex
            v = e.targetvertex

            if d.find(u.node) is not d.find(v.node):              #if they are not in the same set i.e. if they are disjoint
                spanningtrees.append(e)                           #add them to the set
                d.merge(u.node, v.node)                           #if it is a tree merge it

        for e in spanningtrees:
            print(e.startvertex.name, " - ", e.targetvertex.name) #print the connection one by one for all edges

v1 = Vertex("A")
v2 = Vertex("B")
v3 = Vertex("C")
v4 = Vertex("D")
v5 = Vertex("E")
v6 = Vertex("F")
v7 = Vertex("G")

e1 = Edge(2, v1, v2)
e2 = Edge(6, v1, v3)
e3 = Edge(5, v1, v5)
e4 = Edge(10, v1, v6)
e5 = Edge(3, v2, v4)
e6 = Edge(3, v2, v5)
e7 = Edge(1, v3, v4)
e8 = Edge(2, v3, v6)
e9 = Edge(4, v4, v5)
e10 = Edge(5, v4, v7)
e11 = Edge(5, v6, v7)

vertexlist = []
vertexlist.append(v1)
vertexlist.append(v2)
vertexlist.append(v3)
vertexlist.append(v4)
vertexlist.append(v5)
vertexlist.append(v6)
vertexlist.append(v7)


edgelist = []
edgelist.append(e1)
edgelist.append(e2)
edgelist.append(e3)
edgelist.append(e4)
edgelist.append(e5)
edgelist.append(e6)
edgelist.append(e7)
edgelist.append(e8)
edgelist.append(e9)
edgelist.append(e10)
edgelist.append(e11)

k = Kruskal()
k.spanningtree(vertexlist, edgelist)