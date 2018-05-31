'''n1 = 48
n2 = 36

# find smaller
if (n1 > n2):
    smaller = n2
else:
    smaller = n1

# getting hcf
i = 1
while (i <= smaller):
    if (n1 % i == 0 and n2 % i == 0):
        hcf = i
    i = i + 1

print("hcf = ", hcf)'''

# Method 2: Using Recursion
'''
def find_hcf(n1, n2):
    if (n2 == 0):
        return n1
    else:
        return find_hcf(n2, n1 % n2)


n1 = 48
n2 = 36

hcf = find_hcf(n1, n2)
print("highest common factor = ", hcf) '''


#  Method 3: Using math.gcd()

'''
 import math

 n1 = 48
 n2 = 36
 hcf = math.gcd(n1,n2)
 print("Highest Common Factor = ", hcf) '''

# method 4

# implementing Euclidean algo
def get_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


n1 = 48
n2 = 36

hcf = get_gcd(n1, n2)
print("Highest Common Factor = ", hcf)
