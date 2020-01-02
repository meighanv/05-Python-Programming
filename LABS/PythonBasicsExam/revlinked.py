class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Two cases, empty list and list with items
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.prev = None
            self.head = newNode            
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            newNode.prev = probe
            probe.next = newNode

    def print_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    # def insert_node(self, index, data):
    #     probe = self.head
    #     while probe != None:
    #         if probe.next is None and probe.data == index:
    #             self.prepend(data)
    #         elif probe.next == index:
    #             newNode = Node(data)
    #             prev = probe.prev
    #             prev.next = newNode
    #             newNode.next = probe
    #             newNode.prev = prev
    #         probe = probe.next
    
    def reverse(self):
        probe = self.head
        while probe != None:
            if probe.prev == None:
                probe.prev = probe.next
                probe.next = None
                probe = probe.prev
            else:
                temp = probe.prev
                probe.prev = probe.next
                probe.next = temp
                if probe.prev == None:
                    self.head = probe
                    break
                else:
                    probe = probe.prev

        # implement this function

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("A")
doubly_linked_list.append("b")
doubly_linked_list.append([7,245,8,68,"hello"])
#doubly_linked_list.insert_node(1, "one")
doubly_linked_list.print_list()
doubly_linked_list.reverse()
doubly_linked_list.print_list()