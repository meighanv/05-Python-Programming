# Generators

def myGenerator():
    print('First item')
    yield 10
    # These cannot contain 'return' unless you wan to stop the generatator at a specific point 

    print('Second item')
    yield 20

    print('Third item')
    yield 30

gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))

