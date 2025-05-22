# fibbonacci series --> Every term is a sum of last two number. 

n = int(input("Enter the number:- "))
a = 0
b = 1
print(a, b, end = ' ')
for i in range(2,n): 
    c = a+b
    a = b
    b = c
    print(c, end = " ")
    