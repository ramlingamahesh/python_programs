# import complex math module
import cmath

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print('The solution are {0} and {1}'.format(sol1, sol2))

'''

Quadratic equation:

Quadratic equation is made from a Latin term "quadrates" which means square. It is a special type of equation having the form of:

ax2+bx+c=0
Here, "x" is unknown which you have to find and "a", "b", "c" specifies the numbers such that "a" is not equal to 0. If a = 0 then the equation becomes liner not quadratic anymore.

In the equation, a, b and c are called coefficients.

Let's take an example to solve the quadratic equation 8x2 + 16x + 8 = 0
'''