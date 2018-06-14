# Python Program - Pattern Program 14

incr = 1
val = 65
for i in range(0, 5):
    for j in range(0, incr):
        ch = chr(val)
        print(ch, end=" ")
        val = val + 1
    incr = incr + 2
    print()

    '''
A 
B C D 
E F G H I 
J K L M N O P 
Q R S T U V W X Y
    
    '''