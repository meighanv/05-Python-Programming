'''

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:
        The left sub-tree of a node has a value less than its parent node's value.
        The right sub-tree of a node has a value greater than to its parent node's value.
        In this scenario, no duplicate values are allowed.
        
Task #1

Write the fucntion buildBST that receives a list of integers. The function will build The
BST by:
    1. Iterating the list
    2. Using the provided Node class and creating Nodes for each value
    3. Inserting each Node into the BST.
If a value in the list is already in the BST, ignore the value and continue processing the rest of the list.

When complete, the function will return a reference to the root node of the BST.

Task #2

Write the function findLevel that receives the root of a BST (root) and a integer 
value (findVal). The function will search the BST and find and return level of the
BST where the value resides.  If the value is not found, the function returns None.

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.level = 0
        self.right = None
        self.left = None

    # Defining a recursive function the will perform the heavy lifting
    # of the search tree 
    def insert(self, data):
        # This is checking to see if the data is already present in the
        # tree and returns False if it is there 
        if self.val == data:
            return False
        # Checks the data arg against the current node value
        elif self.val > data:
            # If a left node exists, recursively calls insert passing data
            if self.left:
                return self.left.insert(data)
            # Otherwise a node is added
            else:
                self.left = Node(data)
                self.left.level = self.level + 1
                return True
        # If data is greater than current value
        else:
            # If a right node exists, it passes data recursively to insert
            if self.right:
                return self.right.insert(data)
            # Otherwise it creates and adds a new right node
            else:
                self.right = Node(data)
                self.right.level = self.level + 1
                return True

    def find(self, data):
        if (self.val == data):
            return self
        # Checks the data arg against the current node value
        elif self.val > data:
            #checks if left node exists
            if self.left:
                # if so, recursively calls the node find function on Node
                return self.left.find(data)
            else:
                #Otherwise this is the bottom of the tree and data is not present
                return False
        # search to the right
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.val))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.val))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.val))
            if self.right:
                self.right.inorder()
            

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        # If root exists then it calls Node find function on that node
        if self.root:
            return self.root.find(data)
        # Otherwise it returns False b/c the data is not in the tree
        else:
            return False

    def preorder(self):
        print("Preorder")
        self.root.preorder()
    
    def postorder(self):
        print("Postorder")
        self.root.postorder()

    def inorder(self):
        print("Inorder")
        self.root.inorder()


def buildBST(nums):
    bst = Tree()
    for num in nums:
        bst.insert(num)
    return bst.root



def findLevel(root, findVal):
    targnode = root.find(findVal)
    if targnode:
        return targnode.level
    return None

