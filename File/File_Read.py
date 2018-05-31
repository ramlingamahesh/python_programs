# Python Program - Read a File

print("Enter 'x' for exit.");
filename = input("Enter file name (with extension) to read: ");
if filename == 'x':
    exit();
else:
    c = open("C://Users//vramlma//Documents//body.txt", "r");
    print("\nThe file,",filename,"opened successfully!");
    print("The file",filename,"contains:\n");
    print(c.read())
    c.close()