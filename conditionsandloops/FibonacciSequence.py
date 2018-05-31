'''

The Fibonacci sequence specifies a series of numbers where the next number is found by adding up the two numbers just before it.

For example:


0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on...

'''

nterms = int(input("How many terms you want? "))
# first two terms
n1 = 0
n2 = 1
count = 2
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   print(n1,",",n2,end=', ')
   while count < nterms:
       nth = n1 + n2
       print(nth,end=' , ')
       # update values
       n1 = n2
       n2 = nth
       count += 1