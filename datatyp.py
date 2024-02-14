#datatypes in python

# l=int(input("Enter length:"))
# b=int(input("Enter breadth:"))
# area=l*b
# print(area)

# pie=3.141592653589793238
# r=int(input("Enter the value:"))
# area=pie*r*r
# print(area)

import math
# #power of 2
# a=int(input("Enter any number you think is power of 2:"))
# c=math.sqrt(a)
# print(c)
# if(c.is_integer):
#     print(f"The number {a} is power of 2 and the power is {c}")
# else:
#     print(f"The number {a} is not power of 2")


a = int(input("Enter any number you think is a perfect square: "))
b = math.sqrt(a)

if b.is_integer():
    print(f"The number {a} is a perfect square and its square root is {int(b)}")
else:
    print(f"The number {a} is not a perfect square")


