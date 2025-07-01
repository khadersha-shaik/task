def factorial(n):
    if (n<2):
        return(1)
    else:
        return n*factorial(n-1)

inp=int(input("Enater a number "))
out=factorial(inp)
print(out)
    

print("\n \n \n task 2 \n \n \n ")

import math

inp=int(input("enter a number "))

print(f"Squre root: {math.sqrt(inp)}")
print(f"logarithm: {math.log(inp)}")
print(f"Sine: {math.sin(inp)}")
