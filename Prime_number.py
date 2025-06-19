# prime number are number that is divisible by only 1 and itself 

num = int(input("Enter the number : "))

if num<=1: 
    print("this is not a prime number.")
if num>1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")