classRooms = {  'CS101':'3004',
                'CS102':'4501',
                'CS103':'6755',
                'NT110':'1244',
                'CM241':'1411' }

classInst = {  'CS101':'Haynes',
                'CS102':'Alvarado',
                'CS103':'Rich',
                'NT110':'Burke',
                'CM241':'Lee' }

classTimes = {  'CS101':'8:00 am',
                'CS102':'9:00 am',
                'CS103':'10:00 am',
                'NT110':'11:00 am',
                'CM241':'1:00 pm' }

def main():
    course = getClassNumber(classTimes)
    classInfo(course,classRooms,classInst,classTimes)

def getClassNumber(times):
    displayClass(times)
    course = ''
    while course not in times:
        course = input('Please select a class number from the above catalog:\n')
    return course    

def displayClass(dictionary):
    for key in dictionary:
        print(key)

def classInfo(course,room,inst,time):
    print('Information for {}: '.format(course))
    print('Room:\t\t {}'.format(classRooms[course]))
    print('Instructor:\t {}'.format(classInst[course]))
    print('Time:\t\t {}'.format(classTimes[course]))
    
main()