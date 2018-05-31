# Python Program - Convert Binary to Hexadecimal

print("Enter 'x' for exit.");
binary = input("Enter a number in Binary Format: ");
if binary == 'x':
    exit();
else:
    temp = int(binary, 2);
    print(binary,"in Hexadecimal =",hex(temp));