# This is meant to be a doubly, cirularly linked list to simulate the 
# turns being taken.


# Creating the node class for a player's turn which will hold a player 
# object as data
class PlayerTurn:
    def __init__(self, data, next = None, prev = None):
        # Instantiates a node with a default next of None
        self.data = data # player data object
        self.next = next # will point to next clockwise player
        self.prev = prev # will point to next counter-clockwise player
        
        
class TurnList:
    def __init__(self):
        self.head = None #creating head and tail for the list
        self.tail = None # May not really need tail once it is connected
        self.__direction = 1 # This will indicate the direction the token is moving
        self.__token = None # This will track current player node thus indicating turn
        self.__dealer = None # Marks if this player is currently the dealer
        self.__change = False # Tracks changes made and Unity's state of reflecting change

    # Add a player node to our linked list
    def append(self, data):
        # Instantiate a new node
        newPlayer = PlayerTurn(data)
        
        # Is there something in our linked list yet
        if self.head is None:
            newPlayer.prev = None
            self.head = newPlayer
            self.tail = self.head
        # There are node(s) in our linked list
        else:
            self.tail.next = newPlayer
            newPlayer.prev = self.tail
            self.tail = self.tail.next
    
    # Method to make the list circular once fully populated and place the token at the head
    def complete(self):
        self.head.prev = self.tail
        self.tail.next = self.head
        self.__dealer = self.head
        self.__token = self.__dealer.next

    def nextTurn(self):
        if (self.__direction == 1):
            self.__token = self.__token.next
        else:
            self.__token = self.__token.prev

    def reverse(self):
        if (self.__direction == 1):
            self.__direction = 0
        elif(self.__direction == 0):
            self.__direction = 1

    def skip(self):
        self.nextTurn()
        self.nextTurn()

    def toggleChange(self):
        if (self.__change == False):
            self.__change = True
        elif (self.__change == True):
            self.__change = False

    def printCurrent(self):
        print(self.__token.data)

    # This is meant to return the current player object
    def get_player(self):
        return self.__token.data

def main():
    names = ["player1", "player2", "player3", "player4"]
    turns = TurnList()
    for name in names:
        turns.append(name)
    turns.complete()
    print(turns.get_player())
    turns.nextTurn()
    print(turns.get_player())
    turns.skip()
    print(turns.get_player())
    turns.reverse()
    turns.nextTurn()
    print(turns.get_player())

main()




