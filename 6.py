#Exception and exception handling
a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
try:
    if(a,b!=0):
     c=a/b
     print(f"hello {c}")
except ZeroDivisionError:
     print("cant divide by zero")
