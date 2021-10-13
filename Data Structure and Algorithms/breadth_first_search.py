class Node:                                         #takes O(N) memory

    def __init__(self, name):                       #uses queue
        self.name = name                            #takes it layer by layer
        self.adjlist = []
        self.visited = False
        self.predecessor = None

class Bfs:

    def bfs(self, startnode):
        queue = []
        queue.append(startnode)
        startnode.visited = True                   #mark it as visited

        while queue:

            actual_node = queue.pop(0)
            print("%s" % actual_node.name)

            for n in actual_node.adjlist:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

n1 = Node("a")
n2 = Node("b")
n3 = Node("c")
n4 = Node("d")
n5 = Node("e")

n1.adjlist.append(n2)
n1.adjlist.append(n3)
n2.adjlist.append(n4)
n4.adjlist.append(n5)

b = Bfs()
b.bfs(n1)