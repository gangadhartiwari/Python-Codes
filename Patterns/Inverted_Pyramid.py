# using for loop 

# rows = 5
# for i in range(rows, 0, -1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))


# using while loop

n= int(input("Enter the row number:- "))

i = 0
while i<=n: 
    print(' '*i+ ' *'*(n-i))
    i += 1