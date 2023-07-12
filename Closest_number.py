# Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by M. If there are more than one such number, then output the one having maximum absolute value.

n = int(input("Enter number: "))
m = int(input("Enter number closest to: "))
division = int(n/m) 

modulus = int(n%m) 
next_div = division + m

if(n>=0):
    if(modulus == 0 or modulus == 1):
        print(m*division)
    else:
        print(m*next_div)
else:
    if(modulus == 0 or modulus == 1):
        print("-",m*next_div)
    else:
        print("-",m*modulus)
    
