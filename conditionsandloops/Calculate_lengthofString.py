
# calculate length of a String without using len() function
# User inputs the string and it gets stored in variable str
str = input("Enter a string: ")

# counter variable to count the character in a string
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)






#2 with using len() function

# User inputs the string and it gets stored in variable str
str = input("Enter a string: ")

# using len() function to find length of str
print("Length of the input string is:", len(str))
Output: