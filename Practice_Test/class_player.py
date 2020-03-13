""" Demonstrates: 3.p OOP and Classes"""

import math

""" Create a class Player which represents a character in a game.  The player should have the following attributes:
		name: string representing Paladin's name
		hit_points: float, number of hit points (starts at 100)
		x_pos: int x position on a grid (starts at 0)
		y_pos: int y position on a grid (starts at 0)
		
	Player methods are:
		report_pos: returns a tuple (x_pos, y_pos)
		reduce_health: takes in <float> distance as argument and reduces player hit_points by half the distance.
		move: takes in x_pos and y_pos as arguments, computes the distance by  getting the square root of 
		      (x_pos*x_pos + y_pos*y_pos)
		      calls reduce_health(), and returns hit points.
			- If move is called and it reduces hit_points below 0, return "You are out of hit points!"
		"""
		
''' 

***REVIEWER COMMENTS/APPROVAL****





'''		
'''
*** NOTES FOR REVIEWER***
This prompt assumes that player movement is always a positive movement from current position based on how TestCase1 is written.
The provided formula makes the same assumption which removes the ability to move backwards.
This also assumes that there is no negative space, removing 3 quadrants of a true 2D plane
If multiple moves are to be considered on a true 2D plane and alowwing for backward movement then it is recommended that the 
formula be used:
  math.sqrt((math.fabs(self.x_pos-x_pos)**2 + math.fabs(self.y_pos-y_pos)**2)
  
Aside from all that, the packaged unit test is broken since TestCase3 moves Jokem by 100, 100 which results in taking the 
Sqrt of 20000 which ~= 141 which should result in an "out of hit points" message. This makes sense for the second part of TestCase3.
Based on the expected value in TestCase3 is the exact result if move was to (50,50).  
'''


#based on the original code provided it appeared player was meant to be a subclass of object
class object:
  # Creating a general object class for the theorhetical game
	def __init__(self, objType):
    # Initializing the object type
		self.__objType = objType

# Defining the 'Player' subclass
class Player(object):
  # initializing the player object with provided name, default HP of 100, and position 0,0
	def __init__(self, name, hit_points = 100, x_pos = 0, y_pos = 0 ):
		object.__init__(self, 'Player')
		self.name = name
		self.hit_points = hit_points
		self.__x_pos = x_pos
		self.__y_pos = y_pos
	
  #defining report_position which returns coordinates as a tuple
	def report_pos(self):
		return self.__x_pos, self.__y_pos
	
  #defining the reduce_health method which reduces player object HP by distance arg and returns HP
	def reduce_health(self, distance):
		self.hit_points -= distance
		return self.hit_points

  # defining move method for player
	def move(self, x_pos, y_pos):
    #Calculates the distance assuming start point is always 0,0 based on above prompt
		distance = math.sqrt(x_pos**2 + y_pos**2)
		# Reduces player HP by distance value
    self.reduce_health(distance)
    # Checks to see if HP is depleted
		if self.hit_points < 0:
      # To return 'game over' message 
			return f'You are out of hit points!'
		#sets new position for player
    self.__x_pos += x_pos
		self.__y_pos += y_pos
    #returns player HP
		return self.hit_points

#jokem = Player("Jokem")
#print(jokem.move(100,100))
#print(jokem.report_pos())




		
