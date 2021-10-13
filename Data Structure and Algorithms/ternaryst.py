
class Node(object):

    def __init__(self, character):
            self.character = character
            self.rightnode = None
            self.leftnode = None
            self.middlenode = None
            self.value = 0

class Tst(object):

    def __init__(self):
        self.rootnode = None

    def put(self, key, value):
        self.rootnode = self.insert(self.rootnode, key, value, 0)

    def insert(self, node, key, value, index):

        ch = key[index]

        if node == None:
            node = Node(ch)

        elif ch < node.character:
            node.leftnode = self.insert(node.leftnode, key, value, index)
        elif ch > node.character:
            node.rightnode = self.insert(node.rightnode, key, value, index)
        elif index < len(key)-1:
            node.middlenode = self.insert(node.middlenode, key, value, index+1)
        else:
            node.value = value

        return node

    def get(self, key):

        node = self.getitem(self.rootnode, key, 0)

        if node == None:
            return -1

        return node.value

    def getitem(self, node, key, index):
        
        if node == None:
            return None

        ch = key[index]

        if ch < node.character:
            return self.getitem(node.leftnode, key, index)
        
        elif ch > node.character:
            return self.getitem(node.rightnode, key, index)

        elif index < len(key)-1:
            return self.getitem(node.middlenode, key, index+1)

        else:
            return node

if __name__ == "__main__":

    tst = Tst()
    tst.put("apple", 100)
    tst.put("ora", 30)

    print(tst.get("ora"))