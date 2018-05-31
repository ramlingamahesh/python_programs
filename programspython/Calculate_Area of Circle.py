# Python Program - Calculate Area of Circle

print("Enter 'x' for exit.");
rad = input("Enter radius of circle: ");
if rad == 'x':
    exit();
else:
    radius = float(rad);
    area = 3.14 * radius * radius;
    print("\nArea of Circle = %0.2f" %area);