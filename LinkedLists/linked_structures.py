"""
********************LINKED STRUCTURES************************
A linked structure is a concrete data type that implements many types 
of collections, including lists.

As the name implies, a linked structure consists of items that are 
linked to other items. The two that we'll go over are the Singly/Doubly
Linked structures

- Head Link - the first item of a linked structure
- Tail Link - an external link in a doubly linked structure to access the last item directly
- Empty Link - the absence of a link, indicated by the slash in the diagram

- The last item in either structure has no link to a next item

- Node - The basic unit of representation in a linked structure
    - comprised of atwo items
        - A Data Item
        - A link to the next node in the structure

In python we set up nodes and linked structures by using references to object

"""

"""
1. Using box and pointer notation, draw a picture of the nodes created by the 
first loop in the tester program. 

HEAD -> D1 |BOX| -> D2 |BOX| -> D3 |BOX| -> D4 |BOX| -> D5 |\| 
​
2. What happens when a programmer attempts to access a node’s data fields when 
the node variable refers to None? How do you guard against it?
You could __data upon initialization and create specific methods for accessing 
and mutating the data you need
​
3. Write a code segment that transfers items from a full array to a singly linked 
structure. The operation should preserve the ordering of the items.
​
"""

"""
Core Exercises:
​
    1. Finish out your doubly and circular linked list to add more functionality
        - prepend
        - insert
        - delete
        - print
​
    2. Implement a swap_node method to singly and doubly.
​
    3. Implement a reverse method to singly and doubly.
​
    4. Modify delete to find the data you want to delete rather than an index.
        Modify delete to take in either an index or data.
​
    5. Implement a count_ocurrences method.
​
    6. Create a new file and modify your code to have DoublyLinkedList inherit from your 
        SinglyLinkedList class.
​
Extras Exercises:
​
    7. Define a length function that returns the number of items in your linked structure.
​
    8. Define a function makeDoubly that expects a singly linked structure as its argument. The 
        function builds and returns a doubly linked structure that contains the items in the singly
        linked structure. 
​
"""