def main():
    head = 5
    filename = 'C:\\Users\\student\\Documents\\numbers.txt'
    f = open(filename, 'r')
    a = f.readlines()
    for i in range(head):
        print(a[i], end='')
    
main()