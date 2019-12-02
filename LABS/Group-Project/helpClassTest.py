import helpClass

array = []

for i in range(2):
    desc = input('Description:\n')
    ex1 = input('Example 1:\n')
    ex2 = input('Example 2:\n')
    test = helpClass.HelpObject(desc, ex1, ex2)
    array.append(test)

for i in array:
    print(f'{i.getDesc()}\n{i.getEx1()}\n{i.getEx2()}')

