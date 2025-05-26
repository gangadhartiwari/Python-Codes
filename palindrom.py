#By using slicing

# n = input("Enter any string:- ")

# if (n==n[::-1]):
#     print(f"{n} is palindrom")
# else: 
#     print(f"{n} is not palindrom")




# By using for loop

n= input("Enter the value:- ")
rev = ''
for i in n:
    rev = rev+i

if n == rev: 
    print(f"{n} is palindrom")
else:
    print(f"{n} is not palindrom")