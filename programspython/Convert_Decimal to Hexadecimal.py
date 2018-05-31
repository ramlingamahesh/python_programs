# Python Program - Convert Decimal to Hexadecimal

print("Enter 'x' for exit.");
dec = input("Enter number in Decimal Format: ");
if dec == 'x':
    exit();
else:
    decimal = int(dec);
    print(decimal,"in Hexadecimal =",hex(decimal));