# Testing the node class

from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

#print the contents of the structure
while head != None:
    print(head.data)
    head = head.next

head2 = None
mylist = 'Who Goes There'
for i in range(1,len(mylist)+1):
    head2 = Node(mylist[-i], head2)

while head2 != None:
    print(head2.data)
    head2 = head2.next
"""

- One pointer, head, generates the linked structure. This pointer is 
manipulated in such a way that the mot recently inserted item is always
 at the beginning of the structure
- When the data are displayed, they appear in the reverse order of 
their insertion
- Also, the head pointer is reset to the next node, until the head 
pointer becomes None. Thus, at the end of this process, the nodes are 
effectively deleted from the linked structure. They are no longer 
available to the program and are recylcled during the next garbage 
collection

"""
