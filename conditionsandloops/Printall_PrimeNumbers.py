# Take the input from the user:
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


            # Composite number:
            #
            # Other natural numbers that are not prime numbers are called composite numbers.
            #
            # For example: 4, 6, 9 etc. are composite numbers.