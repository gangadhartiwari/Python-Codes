# for century years we have condition = year%400==0 and year%100==0
# for other years we have condition = year%4 == 0 and year%100 != 0

year = int(input("Enter Year :"))

if (year%400 == 0) and (year%100==0): 
    print(f"{year} is a leap year")
elif (year%4==0) and (year%100 != 0): 
    print(f"{year} is a leap year")
else: 
    print(f"{year} is not a leap year")