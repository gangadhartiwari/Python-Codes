#taking input from user
n = int(input("Enter any number:- "))

#checking for 0 or 1
if (n==0 or n==1):
    print(f"{n} is not a prime number ")
elif n>1: 
    for i in range(2,n):
        print(f"{n} is not a prime number")
        break
    else: 
        print(f"{n} is a prime numnber")
# this else is for negative number
else: 
    print(f"{n} is not a prime number")