# Python Program - Find Sum of Natural Numbers

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