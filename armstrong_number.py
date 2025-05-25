# bu using while loop :- 

n = int(input("Enter any number:- "))
n2 = n
t_digit = len(str(n))
sum = 0

while n>0:
    last_digit = n%10
    sum = sum+(last_digit**t_digit)
    n= n//10
if sum==n2: 
    print(f"{n2} is a armstrong number.")
else: 
    print(f"{n2} is not a armstrong number.")




#by using for loop but while loop is more natural when its come to count the digit 

# n = int(input("Enter any number: "))
# n_str = str(n)
# t_digit = len(n_str)
# sum = 0
# # Using for loop to iterate through each digit
# for digit in n_str:
#     sum += int(digit) ** t_digit

# if sum == n:
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")
