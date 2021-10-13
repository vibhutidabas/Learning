class Node:                                      #takes O(logn) memory 
    
    def __init__(self, name):                    #uses stack
        self.name = name                         #takes it to the left most node
        self.visited = False
        self.adjlist = []

class Dfs:

    def dfs(self, node):

        node.visited = True                      #mark it as visited
        print("%s" % node.name)

        for n in node.adjlist:
            if not n.visited:
                self.dfs(n)                      #recursion is used in this one

n1 = Node("a")
n2 = Node("b")
n3 = Node("c")
n4 = Node("d")
n5 = Node("e")

n1.adjlist.append(n2)
n1.adjlist.append(n3)
n2.adjlist.append(n4)
n4.adjlist.append(n5)

d = Dfs()
d.dfs(n1)