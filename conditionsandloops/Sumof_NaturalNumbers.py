num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate un till zero
    while (num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)


    # 2 Python Program - Find Sum of Natural Numbers

    print("Enter '0' for exit.");
    num = int(input("Upto which number ? "));
    if num == 0:
        exit();
    elif num < 1:
        print("Kindly try to enter a positive number..exiting..");
    else:
        sum = 0;
        while num > 0:
            sum += num;
            num -= 1;
        print("Sum = ", sum);