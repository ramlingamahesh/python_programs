#Method 1: Using int()

#program to add two numbers in python 3
#number1 = input("enter number 1:")
#number2 = input("enter number 2:")
#sum = int(number1) + int(number2)
#print("sum = " , sum)


#Method 2: Using Decimal()

#program to add two numbers in Python 3
import decimal
number1 = input("enter number 1:")
number2 = input("enter number 2:")
sum = decimal.Decimal(number1) + decimal.Decimal(number2)
print("sum = " , sum)

