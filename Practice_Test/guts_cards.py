def isthreeok(hand):
    if (hand[0] == hand[1] and hand[0] == hand[2]):
        return True
    else:
        return False
        
def containsPair(hand):
    if (hand[0] == hand[1] or hand[0] == hand[2] or hand[1] == hand[2]):
        return True
    else:
        return False
        
def compareHigh(hand1, hand2):
    if (max(hand1) > max (hand2)):
        return hand1
    elif (max(hand1) < max (hand2)):
        return hand2
    else:
	    return hand1

def findGutsWinner(hand1, hand2):
    if len(hand1)!=3 or len(hand2)!=3:
        return []
    if (isthreeok(hand1) and isthreeok(hand2)):
        return compareHigh(hand1, hand2)
    elif (isthreeok(hand1) and not isthreeok(hand2)):
        return hand1
    elif (not isthreeok(hand1) and isthreeok(hand2)):
        return hand2
    elif (containsPair(hand1) and containsPair(hand2)):
        return compareHigh(hand1, hand2)
    elif (containsPair(hand1) and not containsPair(hand2)):
        return hand1
    elif (not containsPair(hand1) and containsPair(hand2)):
        return hand2
    else:
        return compareHigh(hand1, hand2)

def main():
    hand1 = [2,4]
    hand2 = [2,1,2]
    print(findGutsWinner(hand1, hand2))
    return

main()
