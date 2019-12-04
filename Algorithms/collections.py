# Collection - a group of zero or more items that can be reated as a 
# conceptual unit. Things like lists, strings, tuples, dictionaries
# 
# Other collection types - stacks queues priority queues binary 
# search trees, heaps, graphs, and bags
# 
# Typically dynamic rather than static with the exception of tuples and strings (immutable)
# 
# linear collection - like people in a line, they are ordered by position.
#                     Each item except the first has a unique predecessor
# 
#       Examples: grocery lists, atm line, stacks of dinner plates 
# 
# Heirarchical collection - ordered in a structure resembling an upside down tree.
#                           Each data item except the one at the top (the root) has
#                           just one predecessor called its parent.but potenitally  
#                           has many successors
# 
#       Examples: File directory system, organizational trees, and a table of contents 
# 
# Graph collection - also called graph, each item can have many predecessors and many 
#                    successors. These are also called neighbors 
# 
#       Examples: include airline routes, electrical wiring diagrams, and WWW
# 
# unordered collections - these are not in any particular order, and its not possible to 
#                         meaninfully speak of an item's predecessor or successor
#       Examples: bag of marbles 
#*****************************OPERATION TYPES**************************************
# Determine the size - like using python's len() to obtain the number of items in the
#                      collection

# Test for item membership - Use Python's in operator to search for a given target
#                            item in the collection. Returns True if the item is found
#                            and False otherwise 
# 
# Traverse collection - Use python's for loop to visit each item in the collections. The 
#                       order which items are visited depends upon the type of collection
# 
# Obtain a string representation - Use Python's str()
# 
# Test for equality - Use Python's == operator to determin if collections are equal. Two
#                    collections are equal if they are of the same type and contain the 
#                    same items. The order in which pairs of items are compared depends 
#                    on the type of collection.
# 
# Concatenate collections - Use Python's + operator to obtain a new collection of the same
#                           type as the operands, and containing the items in each.
# 
# Convert to another type of collection - Create a new collection w/ same items as source
# 
# Insert an item - Add the item to collection, possibly at a given position
# 
# Remove an item - Remove the item from the collection, possibly at a given position
# 
# Replace an utem - Combine removal and insertion into one operation
#  
# Access or retrieve and item - obtain an item, possibly at a given position 