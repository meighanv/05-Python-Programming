## This is a function to walk through
## an list of words (passed as arg) to
## focus word selection for madlib.
def selectWord (x):
    print("Provide a word from this list:")
    #Shows the user the options available
    print(x)
    #Get user input
    userInput = input()
    #Input validation for input matching a list item
    while userInput not in x:
        print("Invalid selection, please retry")
        print(x)
        userInput = input()
    return userInput

nouns = ['dog','leader','house','car','phone','desk']
verbs = ['catches','runs','celebrates','forgets','wins','tests']
preps = ['ahead','behind','above','below','under','over']
adjectives = ['joyful','underwhelming','breezy','hot','fast','slow']
colors = ['gold','purple','green','red','silver','yellow']

print("Hello! Please enter the following: ")
#getting input for each of the terms to be used in the sentences
noun = selectWord(nouns)
noun2 = selectWord(nouns)
verb = selectWord(verbs)
adjective = selectWord(adjectives)
adjective2 = selectWord(adjectives)
prep = selectWord(preps)
color = selectWord(colors)

#taking input and putting them into sentences
print("The {} {} {} {} {} the {} {}!".format(adjective,color,noun,verb,prep,adjective2,noun2))
print("A {} is a {} {} {}!".format(noun,adjective2,color,noun2))
