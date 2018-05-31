# 5 Ways

#1.Using Loop
'''
string1 = "the crazy programmer"
string2 = ""

i = len(string1) - 1

while (i >= 0):
    string2 = string2 + string1[i]
    i = i - 1

print ("original = " + string1)
print ("reverse  = " + string2)
'''

# 2. Using Recursion

'''
def reverse_it(string):
    if len(string) == 0:
        return string
    else:
        return reverse_it(string[1:]) + string[0]
        print
        "added " + string[0]


string1 = "the crazy mad programmer"
string2 = reverse_it(string1)

print ("original = " + string1)
print ("reverse  = " + string2)
'''


#3. Using Stack
'''
def create_stack():
    # it will  create a List named as stack and return it
    stack = []
    return stack


def push(stack, element):
    # it will add a new element to List
    stack.append(element)


def pop(stack):
    # it will delete the last element from  List
    if len(stack) == 0:
        return
    return stack.pop()


def reverse(string):
    # method to reverse the string using stack's functions
    n = len(string)

    # to create a empty list (stack)
    stack = create_stack()

    # inserting character of string into List
    for i in range(0, n):
        push(stack, string[i])

    # making string empty
    string = ""

    # getting last element of the List (stack) and storing it into string
    for i in range(0, n):
        string = string + pop(stack)
    return string


string1 = "the mad crazy programer"
string2 = reverse(string1)

print ("original = " + string1)
print ("reverse  = " + string2)

'''
#In above  program, we’re using concept of stack having push and pop functions.


# 4. Using Extended Slice
'''
string = "the crazy programmers"
print("original = " + string)

string = string[::-1]
print("reversed = " + string) '''


#5. Using List


string = "the crazy PPprogrammer"
print("original = " + string)

# convrting string into list
list1 = list(string)

# applying reverse method of list
list1.reverse()

# converting list into string
string = ''.join(list1)
print("reversed = " + string)