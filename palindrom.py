#By using slicing

n = input("Enter any string:- ")

if (n==n[::-1]):
    print(f"{n} is palindrom")
else: 
    print(f"{n} is not palindrom")