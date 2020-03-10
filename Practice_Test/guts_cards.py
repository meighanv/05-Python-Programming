#This function takes a list of integers and compares each of the element
# to find three of a kind. Returns True if the calue of each element is equal
def isthreeok(hand):
    # If the first card is equal to each of the others then it is three of a
    # kind
    if (hand[0] == hand[1] and hand[0] == hand[2]):
        return True
    else:
        return False

#This function checks for a pair in a list
def containsPair(hand):
    # Check to see if any of the elements are equal in an expected 3 element list
    if (hand[0] == hand[1] or hand[0] == hand[2] or hand[1] == hand[2]):
        return True
    else:
        return False
# This compares the value of the highest card in each of the two hands        
def compareHigh(hand1, hand2):
    if (max(hand1) > max (hand2)):
        return hand1
    elif (max(hand1) < max (hand2)):
        return hand2
    else:
	    return hand1

#Function to compare two hands to return the winning hand
def findGutsWinner(hand1, hand2):
    # check to ensure each hand has a size of three
    if len(hand1)!=3 or len(hand2)!=3:
	#if either hand size != 3 then return the empty list
        return []
    #Checking if both hands are three of a kind
    if (isthreeok(hand1) and isthreeok(hand2)):
	# In this case, return the hand with the highest card
        return compareHigh(hand1, hand2)
    #The next two return the hand that is three of a kind if the other is not
    elif (isthreeok(hand1) and not isthreeok(hand2)):
        return hand1
    elif (not isthreeok(hand1) and isthreeok(hand2)):
        return hand2
    # Checking to see if both hands contain a pair
    elif (containsPair(hand1) and containsPair(hand2)):
        # If they both contain pairs return the hand with highest card
	return compareHigh(hand1, hand2)
    # The next two return the hand that has the pair if the other does not
    elif (containsPair(hand1) and not containsPair(hand2)):
        return hand1
    elif (not containsPair(hand1) and containsPair(hand2)):
        return hand2
    #When the hands contain neither three of a kind or a pair, 
    #return the hand with the high card
    else:
        return compareHigh(hand1, hand2)

## Manual testing of code
#def main():
#    hand1 = [2,4]
#    hand2 = [2,1,2]
#    print(findGutsWinner(hand1, hand2))
#    return
#
#main()
