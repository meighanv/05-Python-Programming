# Doubly Linked Lists - Very similar to Single linked lists these have 
#                       prev pointer and a tail node
#   Move left, to previous node, from a given node 
#   Move immediately to the last node

class DoubleNode:
    def __init__(self, data, next = None, prev = None):
        # Instantiates a node with a default next of None
        self.data = data
        self.next = next
        self.prev = prev

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    # printing our linked list
    def printLinked(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    # printing our linked list reversed starting from tail
    def printReverse(self):
        probe = self.tail
        while probe != None:
            print(probe.data)
            probe = probe.prev

    # To add something to our linked list
    def append(self, data):
        # Instantiate a new node
        newNode = DoubleNode(data)
        # Is there something in our linked list yet
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.tail = self.head
        # There are node(s) in our linked list
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next
           
    
    # Add to beginning (prepend)
    def prepend(self, data):
        #instantiate a new node
        newNode = DoubleNode(data)
        # Anything in our linked list
        newNode.next = self.head
        self.head = newNode

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

    def insert(self, index, data):
        # If empty or index is less than 1
        if self.head is None or index <= 0:
            self.head = DoubleNode(data, self.head)
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # Insert new node after the node at position index -1 or last position 
            # Setting the new node as the Next for current position
            # New node points to current position as prev and current next as next 
            probe.next = DoubleNode(data, probe.next, probe)
            # Advance to new node
            probe = probe.next
            # Reset the previous of next node to point to probe (inserted node)
            probe.next.prev = probe
    
    # Swapping the data at specified indicies with first node being 0
    # Too High of an index results in the last element being involved
    # in the swap. 
    def swapNode(self, index1, index2):
        # Setting and moving a probe for the 1st item
        probe1 = self.head
        while index1 > 0 and probe1.next != None:
            probe1 = probe1.next
            index1 -= 1
        # storing data for probe1 in tempData
        tempData = probe1.data
        # Setting and moving the probe for the second item
        probe2 = self.head
        while index2 > 0 and probe2.next != None:
            probe2 = probe2.next
            index2 -= 1
        # swapping the data elements of each node
        probe1.data = probe2.data
        probe2.data = tempData

    def reverse(self):
        probe = self.tail
        while probe != None:
            temp = probe.next
            probe.next = probe.prev
            probe.prev = temp
            probe = probe.next
        temp = self.tail
        self.tail = self.head
        self.head = temp
            # temp = head.data
            # head.data = tail.data
            # tail.data = temp
            # head = head.next
            # tail = tail.prev
            # if head.prev != None and head.prev == tail.next or head == tail:
            #     break

    def getIndex(self, index):
        # If empty or index is less than 1
        probe = self.head
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
            # Insert new node after the node at position index -1 or last position 
        print(probe.data)

    def __len__(self):
        probe = self.head
        count = 1
        while probe.next != None:
            probe = probe.next
            count += 1
        return count

dublink = DLList()
dublink.append("A")
dublink.append("B")
dublink.append("C")
dublink.append("D")
dublink.append("E")
dublink.append("F")
#dublink.prepend([9,8,7,6])
#dublink.insert(2, "WhoDey")
dublink.printLinked()
#print(len(dublink))
print()
#dublink.printReverse()
#dublink.delete(2)
print()
dublink.reverse()
dublink.printLinked()


