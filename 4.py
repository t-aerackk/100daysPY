#Today in day 4 i'll learn about conditions in python 

# a=5
# b=5
# if(a>5):
#     print("a is greater than b")
# else:
#     print("B is greater than a.")

#Cable Car ticket counter price
print("Normal ticket cost= 725 rupees")
age=int(input("Enter your age.:"))
if(age<=5):
    print("Your ticket cost is free. ")
elif 10>=age>5:
    f=50/100*725
    print(f"Your ticket cost is 50% off which is {f} rupees. ")
elif 11<=age<=60:
    print("Your ticket cost is 725 rupees. ")
else:
    t=25/100*725
    print(f"Your ticket cost is 25% off whic is {t} rupees.")