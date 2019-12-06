""" 
Stacks are linear collections in which access is completely 
    restricted to just one called top
LIFO - last in first out protocol, (dishes stacked on table)
    push - put item on stack
    pop - remove top item from stack
    peek - examine object on top

    -The stack type is not built into python so we use a list to 
    emulate an array-based stack
    -Going to use the list methos and pop
    -It's possible to utilize other list methods such as insert, 
    replace, and remove but that defeats the purpose of the stack
"""

class Stack:
    def __init__(self):
        self.my_stack = []
    
    def push(self, item):
        self.my_stack.append(item)

    def getStack(self):
        return self.my_stack
    
    def pop(self):
        return self.my_stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.my_stack[-1]

    def is_empty(self):
        return self.my_stack == []


s = Stack()
# s.push("first")
# print(s.getStack())
# s.push("Next one")
# print()
# print(s.getStack())
# s.push("top")
# print()
# print(s.getStack())
# print()
# print(s.pop())
# print()
# print(s.getStack())
# print(s.peek())
# print(s.pop())
# print(s.pop())
# print(s.is_empty())

"""
Use a stack to check whether or not a string has balanced usage of parentheses

Example:
    Balances:  (), ()(), ((({})))
    Unbalanced: ((), {{{)}], [][]]], ([)]
"""
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_bal(paren_string):
    s = Stack()
    is_balanced = True
    # Keep track of where we are
    index = 0
    #loop through the string 
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        #is it an open paren>
        if paren in "({[":
            s.push(paren)
        # it's a closed paren
        elif paren in "})]":
            top = s.pop()
            # The popped item and the current item we're on
            if not is_match(top, paren):
                    #not a match
                    is_balanced = False
        # else:
        #     print("Stop Playin'")
        # increment to evaluate the rest of the string
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

string1 = '(({s}))'
string2 = '{{{)}]'
print(f'String {string1} is balanced: {is_paren_bal(string1)}')
print(f'String {string2} is balanced: {is_paren_bal(string2)}')