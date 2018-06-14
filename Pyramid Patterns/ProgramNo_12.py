# Python Program - Pattern Program 12

num = 1
incr = 1
for i in range(0, 5):
    for j in range(0, incr):
        print(num, end=" ")
        num = num + 1
    print()
    incr = incr + 2

    '''
1 
2 3 4 
5 6 7 8 9 
10 11 12 13 14 15 16 
17 18 19 20 21 22 23 24 25
    '''