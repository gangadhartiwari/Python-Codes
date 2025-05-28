# By using for loop

n= int(input("Enter the row number:- "))

for i in range(1, n+1): 
    print(' '*(n-i)+ ' *'*i)