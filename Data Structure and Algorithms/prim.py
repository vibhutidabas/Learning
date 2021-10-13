import heapq

class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.visited = None
        self.adjlist = []

    def __str__(self):
        return self.name

class Edge(object):

    def __init__(self, weight, startvertex, targetvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex

    def __lt__(self, otheredge):
        selfpriority = self.weight
        otheredge_priority = otheredge.weight
        return selfpriority < otheredge_priority

class PrimsJarnik(object):

    def __init__(self, unvisitedlist):
        self.unvisitedlist = unvisitedlist
        self.spanningtree = []
        self.edgeheap = []
        self.fullcost = 0

    def calctree(self, vertex):

        self.unvisitedlist.remove(vertex)

        while self.unvisitedlist:

            for e in vertex.adjlist:
                if e.targetvertex in self.unvisitedlist:
                    heapq.heappush(self.edgeheap, e)

            minedge = heapq.heappop(self.edgeheap)

            if minedge.targetvertex in self.unvisitedlist:
                self.spanningtree.append(minedge)
                print("Edge added to spanning tree: %s-%s"%(minedge.startvertex.name, minedge.targetvertex.name))
                self.fullcost += minedge.weight
                vertex = minedge.targetvertex
                self.unvisitedlist.remove(vertex)

    def getspanningtree(self):
        return self.spanningtree
    
    def getcost(self):
        return self.fullcost

vertexA = Vertex("A")
vertexB = Vertex("B")
vertexC = Vertex("C")
vertexD = Vertex("D")
vertexE = Vertex("E")
vertexF = Vertex("F")
vertexG = Vertex("G")
 
edgeAB = Edge(2, vertexA, vertexB)
edgeBA = Edge(2, vertexB, vertexA)
edgeAE = Edge(5, vertexA, vertexE)
edgeEA = Edge(5, vertexE, vertexA)
edgeAC = Edge(6, vertexA, vertexC)
edgeCA = Edge(6, vertexC, vertexA)
edgeAF = Edge(10, vertexA, vertexF)
edgeFA = Edge(10, vertexF, vertexA)
edgeBE = Edge(3, vertexB, vertexE)
edgeEB = Edge(3, vertexE, vertexB)
edgeBD = Edge(3, vertexB, vertexD)
edgeDB = Edge(3, vertexD, vertexB)
edgeCD = Edge(1, vertexC, vertexD)
edgeDC = Edge(1, vertexD, vertexC)
edgeCF = Edge(2, vertexC, vertexF)
edgeFC = Edge(2, vertexF, vertexC)
edgeDE = Edge(4, vertexD, vertexE)
edgeED = Edge(4, vertexE, vertexD)
edgeDG = Edge(5, vertexD, vertexG)
edgeGD = Edge(5, vertexG, vertexD)
edgeFG = Edge(3, vertexF, vertexG)
edgeGF = Edge(3, vertexG, vertexF)
 
unvisitedlist = []
unvisitedlist.append(vertexA)
unvisitedlist.append(vertexB)
unvisitedlist.append(vertexC)
unvisitedlist.append(vertexD)
unvisitedlist.append(vertexE)
unvisitedlist.append(vertexF)
unvisitedlist.append(vertexG)
 
vertexA.adjlist.append(edgeAB)
vertexA.adjlist.append(edgeAC)
vertexA.adjlist.append(edgeAE)
vertexA.adjlist.append(edgeAF)
vertexB.adjlist.append(edgeBA)
vertexB.adjlist.append(edgeBD)
vertexB.adjlist.append(edgeBE)
vertexC.adjlist.append(edgeCA)
vertexC.adjlist.append(edgeCD)
vertexC.adjlist.append(edgeCF)
vertexD.adjlist.append(edgeDB)
vertexD.adjlist.append(edgeDC)
vertexD.adjlist.append(edgeDE)
vertexD.adjlist.append(edgeDG)
vertexE.adjlist.append(edgeEA)
vertexE.adjlist.append(edgeEB)
vertexE.adjlist.append(edgeED)
vertexF.adjlist.append(edgeFA)
vertexF.adjlist.append(edgeFC)
vertexF.adjlist.append(edgeFG)
vertexG.adjlist.append(edgeGD)
vertexG.adjlist.append(edgeGF)
 
algorithm = PrimsJarnik(unvisitedlist)
algorithm.calctree(vertexD)
print(algorithm.getcost())