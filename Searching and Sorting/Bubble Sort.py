Arr = [21, 14, 18, 25, 9]
n = len(Arr)  # length

Pass = 1

while (Pass <= n - 1):
    index = 0
    while (index <= n - Pass - 1):
        if Arr[index] > Arr[index + 1]:
            Arr[index], Arr[index + 1] = Arr[index + 1], Arr[index]  # swapping

        index = index + 1

    Pass = Pass + 1

for item in Arr:
    print
    item