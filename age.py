#Take input from user for age and send a message including years until 100
age=str(input("Enter your current age:\n"))
print(type(age))
age=int(age)
print(f"You are {age} years old")
print(type(age))
print(f"You have {100-age} years to beat century")