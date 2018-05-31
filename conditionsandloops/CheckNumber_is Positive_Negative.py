num = float(input("Enter a number: "))

if num > 0:
    print("{0} is a positive number".format(num))
elif num == 0:
    print("{0} is zero".format(num))
else:
    print("{0} is negative number".format(num))



    #2 :method :

    # User enters the number :

    number = int(input("Enter number: "))

    # checking the number
    if number < 0:
        print("The entered number is negative.")
    elif number > 0:
        print("The entered number is positive.")
    elif number == 0:
        print("Number is zero.")
    else:
        print("The input is not a number")