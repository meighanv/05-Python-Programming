# 1. Write a tester program that counts and displays the number of iterations 
#     of the following loop: 

def work():
    size = 100000
    while size > 1:
        #start = time.time()
        size = size // 2
        #elapsed = time.time() - start
        #print(f'{size}')
    print('##################') 

import time
import timeit

problemSize = [1000, 2000, 4000, 10000, 100000]

# for size in problemSize:
#     num = 0
#work()
total_time = timeit.timeit(work, number=1000)
print(total_time)
    # while size > 0:
    #     start = time.time()
    #     size = size // 2
    #     num += 1
    #     elapsed = time.time() - start
    #     print(f'{size} - {elapsed} - {num}')
    # print('##################')

for i in range(50):
    print(f'{i} - {2**i} - {i**4}')


# Comparing time complexity between 2^i and i^4 to determine when 
# i^4 becomes more efficient
x = False
i = 2
while x == False:
    print(f'{i} - {2**i} - {i**4}')
    if 2**i > i**4:
        x = True
        print(f'{i} - {2**i} - {i**4}')
    i += 1


z = False
i = 2
while z == False:
    x = i**2
    y = 0.5*(i**2) + (0.5)*i
    print(f'{i} - {x} - {y}')
    if x < y:
        z = True
        print(f'{i} - {x} - {y}')
    i += 1

    
