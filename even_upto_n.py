n = int(input("Enter any number:- "))  # Takes input from the user and converts it to an integer

for i in range(1, n+1):               # Loops from 1 to n (inclusive)
    if i % 2 == 0:                     # Checks if the number is even
        print(i, end=" ")             # Prints the even number on the same line
