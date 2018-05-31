arr = [4, 8, 19, 2, 28, 21]

min = 0  # set min = 0
n = len(arr)

while (min <= n - 1):
    s_i = min
    while (s_i <= n - 1):  # finding minimum
        if (arr[s_i] < arr[min]):
            arr[min], arr[s_i] = arr[s_i], arr[min]  # swapping element at start index with minimum
        s_i = s_i + 1

    min = min + 1

for element in arr:
    print
    element


    # Output
    #
    # 2 4 8 19 21 28