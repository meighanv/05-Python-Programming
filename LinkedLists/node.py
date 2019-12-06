# This class will represent a singly linked node

class Node:
    def __init__(self, data, next = None):
        # Instantiates a node with a default next of None
        self.data = data
        self.next = next

# This is meant to instantiate nodes and we'll add methods to this 
# class to add functionality
class LinkedList:
    def __init__(self):
        self.head = None
    
    # printing our linked list
    def printLinked(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
    
    # To add something to our linked list
    def append(self, data):
        # Instantiate a new node
        newNode = Node(data)
        # Is there something in our linked list yet
        if self.head is None:
            self.head = newNode
        # There are node(s) in our linked list
        else:
            # Initialize our probe pointer
            probe = self.head
            # Is probe at the end of list?
            while probe.next != None:
                probe = probe.next
            probe.next = newNode

    # Add to beginning (prepend)
    def prepend(self, data):
        #instantiate a new node
        newNode = Node(data)
        # Anything in our linked list
        newNode.next = self.head
        self.head = newNode

    # Inserting within a linked list
    def insert(self, index, data):
        # If empty or index is less than 1
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
                # Insert new node after the node at position index -1 or last position 
            probe.next = Node(data, probe.next)

    def delete(self, index):
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
            return removedItem

    # Swapping the data at specified indicies with first node being 0
    # Too High of an index results in the last element being involved
    # in the swap. 
    def swapNode(self, index1, index2):
        # Setting and moving a probe for the 1st item
        probe1 = self.head
        while index1 > 0 and probe1.next != None:
            probe1 = probe1.next
            index1 -= 1
        # Setting and moving the probe for the second item
        probe2 = self.head
        while index2 > 0 and probe1.next != None:
            probe1 = probe1.next
            index2 -= 1
        # swapping the data elements of each node
        tempData = probe1.data
        probe1.data = probe2.data
        probe2.data = tempData

    # This actually reverses the elements by swaping the data
    # this preserves all the pointers 
    #  
    def reverse(self):
        # Sets an empty list to store the elements
        templist = []
        probe = self.head
        # Moving through the linked list and adding the data elements
        # in existing order to the tempList 
        while probe.next != None:
            templist.append(probe.data)
            probe = probe.next
        templist.append(probe.data)
        
        # After resetting the probe
        probe = self.head
        # Sets the index for loop termination of all elements in tempList
        index = len(templist)
        # Walking backwards through tempList and forward through the
        # linked list to reset each .data to the element stored in 
        # tempList 
        while index > -1 and probe != None:
            probe.data = templist[index-1]
            probe = probe.next
            index -=1
            


    def getIndex(self, index):
        # If empty or index is less than 1
        probe = self.head
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
            # Insert new node after the node at position index -1 or last position 
        print(probe.data)

    def copy(self):
        newLL = LinkedList()
        probe = self.head
        while probe is not None:
            newLL.append(probe.data)
            probe = probe.next
        return newLL

    def __len__(self):
        probe = self.head
        count = 1
        while probe.next != None:
            probe = probe.next
            count += 1
        return count

"""
Circular Linked List - Special case of singly linked list
            Insertion and removal of the first node are special cases of
            the insert ith and remove ith operations on a singly linked 
            list. These are special b/c the head pointer must be reset. 
            You can use circular liked lists with a dummy header node. 
            Contains a link from the last node back to the first node in
            the structure.
"""

class CircLinked:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else: 
            newNode = Node(data)
            probe = self.head
            while probe.next != self.head:
                probe = probe.next
            probe.next = newNode
            newNode.next = self.head
    


linked = LinkedList()
linked.append("A")
linked.append("B")
linked.append("C")
linked.append("D")
linked.append("E")
linked.append("F")
#linked.prepend("I Should be at the beginning")
#linked.insert(2, "This I inserted")
#linked.insert(67, "I inserted this too, with a high index")
# #linked.getIndex(1)
# linked.printLinked()
# print('\n')
# #print(len(linked))
# #linked.delete(1)
# #linked.getIndex(1)
# #linked.printLinked()
# #print(len(linked))
# #linked.swapNode(0,67)
# linked.reverse()
# linked.printLinked()

linked2 = linked.copy()
linked.delete(2)
linked.printLinked()
linked2.printLinked()
    