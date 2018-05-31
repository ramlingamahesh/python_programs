def Binary_search(arr, start_index, last_index, element):
    while (start_index <= last_index):
        mid = (int)(start_index + last_index) / 2
        if (element > arr[mid]):
            start_index = mid + 1
        elif (element < arr[mid]):
            last_index = mid - 1
        elif (element == arr[mid]):
            return mid
    return -1


arr = [2, 14, 19, 21, 99, 210, 512, 1028, 4443, 5110]
element = 4443
start_index = 0
last_index = len(arr) - 1
found = Binary_search(arr, start_index, last_index, element)
if (found == -1):
    print
    "element not present in array"
else:
    print
    "element is present at index " + str(found)

# is a way of programming or coding a problem, in which a function calls itself one or more times in its body.
# #Usually, it is returning the return value of this function call.
# If a function definition fulfils the condition of recursion, we call this function a recursive function

#Recursive Approach (Using Recursion):

'''def Binary_search(arr, start_index, last_index, element):
    mid = (int)(start_index + last_index) / 2

    if (start_index > last_index):
        print
        "Element not found"

    elif (element > arr[mid]):
        start_index = mid + 1
        Binary_search(arr, start_index, last_index, element)

    elif (element < arr[mid]):
        last_index = mid - 1
        Binary_search(arr, start_index, last_index, element)

    else:
        print
        "element is present at index " + str(mid)


arr = [2, 14, 19, 21, 99, 210, 512, 1028, 4443, 5110]
element = 99
start_index = 0
last_index = len(arr) - 1
Binary_search(arr, start_index, last_index, element) '''
