Arr = [5, 14, 18, 6, 21]
n = len(Arr)
i = 1
while (i <= n - 1):
    value = Arr[i]
    position = i

    while (position > 0 and Arr[position - 1] > value):
        Arr[position] = Arr[position - 1]
        position = position - 1

    i = i + 1
    Arr[position] = value

for i in Arr:
    print
    i,

#Output
'''
5
6
14
18
21 '''