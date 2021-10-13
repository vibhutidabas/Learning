class Node:

    def __init__(self, data, parent):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.parent = parent

class Bst:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:                                      #if it is the first element
            self.root = Node(data, None)                           #creates first node
        
        else:
            self.insert_node(data, self.root)                      #insertion starts
            
    #O(logN) but only if the tree is balanced
    def insert_node(self, data, node):

        if data < node.data:                                       #if the element is smaller than the parent i.e. left child
            if node.leftchild:                                     #end tak ja jab tak left child hai
                self.insert_node(data, node.leftchild)
            else:
                node.leftchild = Node(data, node)                  #found the place and now inserting
        
        else:
            if node.rightchild:                                    #same as leftchild but this is greater than the parent
                self.insert_node(data, node.rightchild)
            else:
                node.rightchild = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftchild:                                         
            self.traverse_in_order(node.leftchild)                  #go to the last leftnode

        print('%s' % node.data)                                     #likhker dekhle logic yaha nhi likh sakti

        if node.rightchild:
            self.traverse_in_order(node.rightchild)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        actual = self.root

        while actual.rightchild is not None:
            actual = actual.rightchild

        return actual.data

    def get_predecessor(self, node):
        if node.rightchild:
            return self.get_predecessor(node.rightchild)
        
        return node

    def remove_node(self, data,node):
        if node is None:
            return

        if data < node.data:                                        #if it is a single leftnode
            self.remove_node(data, node.leftchild)
        
        elif data >node.data:                                       #if it is a single rightnode
            self.remove_node(data, node.rightchild)
        
        else:

            if node.leftchild is None and node.rightchild is None:  #leaf node
                print("removing a leaf node....%d" % node.data)

                parent = node.parent

                if parent is not None and parent.leftchild == node:
                    parent.leftchild = None                          #left leaf node removed
                if parent is not None and parent.rightchild == node:
                    parent.rightchild = None                         #right leaf node removed
                
                if parent is None:
                    self.root = None
                del node

            elif node.leftchild is None and node.rightchild is not None: #it has a rightchild
                print("removing a node with single right child")

                parent = node.parent
                if parent is not None:
                    if parent.leftchild == node:
                        parent.leftchild = node.rightchild
                    if parent.rightchild == node:
                        parent.rightchild = node.rightchild
                
                else:
                    self.root = node.rightchild

                node.rightchild.parent = parent
                del node

            elif node.rightchild is None and node.leftchild is not None: #it has a leftchild
                print("removing a node with a single left node")

                parent = node.parent
                if parent is not None:
                    if parent.leftchild == node:
                        parent.leftchild = node.leftchild
                    if parent.rightchild == node:
                        parent.rightchild = node.leftchild

                else:
                    self.root = node.leftchild

            else:                                                       #it has left and right children both
                print("removing node with two child")

                p = self.get_predecessor(node.leftchild)                #predecessor is the largest element in left branch

                temp = p.data                                           #swap the node with the predecessor
                p.data = node.data                                      #after this the node becomes a leaf node and it gets easier to remove it
                node.data = temp

                self.remove_node(data, p)

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

bst = Bst()
bst.insert(5)
bst.insert(-5)
bst.insert(1)
bst.insert(99)
bst.insert(34)
bst.insert(1000)

print("max item : %d" % bst.get_max(bst.root))

bst.traverse()
print("removing a node")
bst.remove(5)
bst.traverse()