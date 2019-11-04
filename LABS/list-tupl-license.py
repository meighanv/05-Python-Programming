#Setting list of correct answers
answers = ['b','d','a','a','c','a','b','a','c','d','b','c','d','a','d','c','c','b','d','a']

def main():
    #Getting filename from input for filename
    filename = input('Provide the file name of the test:\n')
    #Reads the file of filename 
    f = open(filename, 'r')
    #Recording file contents in array
    contents = f.readlines()
    incorrect = []
    total = 0
    total = int(gradeTest(contents,answers,incorrect))
    scoreTest(total,incorrect)
    

def gradeTest(test,answers,incorrect):
    total = 0
    for i in range(len(answers)):
        if test[i].lower().rstrip('\n') == answers[i].lower():
            total += 1
        else:
            incorrect.append(i+1)
    return total

def scoreTest(total,incorrect):
    if total/len(answers) >= 0.75:
        print('You passed!')
        print('You got {} of {} correct.'.format(total,len(answers)))
    else:
        print('You failed!')
        print('You got {} of {} correct.'.format(total,len(answers)))
        print('Questions missed: ', incorrect)
        
main()
