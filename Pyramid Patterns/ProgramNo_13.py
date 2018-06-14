# Python Program - Pattern Program 13

num = 1
count = 0
decr = 8
for i in range(0, 5):
    for k in range(0, decr):
        print(end=" ")
    for j in range(0, i):
        count = count + 1
    num = count
    temp = num
    for j in range(0, i):
        print(num, end=" ")
        num = num - 1
    print()
    num = temp
    decr = decr - 2

    '''
      1 
    3 2 
  6 5 4 
10 9 8 7 
    
    '''