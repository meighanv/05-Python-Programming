# This class will represent a singly linked node

class Node():
    def __init__(self, data, next = None):
        # Instantiates a node with a default next of None
        self.data = data
        self.next = next

# #just and empty link
# node1 = None

# # A Node containing data and an empty link
# node2 = Node("A", None)
# node3 = Node("B", node2)

# print(node3.data)