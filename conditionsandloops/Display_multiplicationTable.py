num = int(input("Show the multiplication table of? "))
# using for loop to iterate multiplication 10 times
for i in range(1,21):
   print(num,'x',i,'=',num*i)

   # 2 Python Program - Print Multiplication Table of a Number

   print("Enter 'x' for exit.");
   num = input("Enter a number: ");
   if num == 'x':
      exit();
   else:
      number = int(num);
      for i in range(1, 11):
         print(number, "*", i, "=", number * i);