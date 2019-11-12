rows = input('Row height')
columns = input('column width')

for i in range(int(rows)):
    for i in range(int(columns)):
        print('#', end='')
        print(' '*i, end='')
        print('#')

