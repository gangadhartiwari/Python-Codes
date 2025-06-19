#squre root of an number using exponential 

n = int(input("Enter the number : "))
sr = n**(1/2)
print(f"The squre root of {n} is : ", sr)


# --------------------------------------------------------------------------
#squre root of an number using inbuilt math function 

import math

n = int(input("Enter The Number :- "))

# sqrt computes the square root
square_root = math.sqrt(n)

print(f"Square Root of {n}  is : ",square_root)



# --------------------------------------------------------------------------

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is : ",power)