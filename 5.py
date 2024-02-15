#Stepping on 5th day of py programming with type casting, 

# a=14
# b=17.29

# c=a+b
# print(c) #automatic conversion or implicit

# c=int(b)+a #manual or explicit
# print(c)

# str1="123"
# num=456
# add=str1+str(num) #string addition
# print(add)
# add2=int(str1)+num
# print(add2)

#lets play true and false
a=str(input("Enter True or False:\n"))
if(a=="True"):
    b=1
    # print("Green Light")
elif a=="False":
    b=0
    # print("Red Light")   
else:
    print("Please Enter True or False only.")
    exit()
print("boolean value:",b)