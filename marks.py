#We are calculating marks of students and grading them accordingly
M=int(input("Enter your total marks obtained:\n"))
p=int(M/5)
print(f"Your total marks obtained is {M} and your percentage is {p}.")

if(p<60):
    print("You have failed the exam.")
elif 60<=p<70:
    print("You are in D grade.")
elif 70<=p<80:
    print("You are in C grade.")
elif 80<=p<90:
    print("You are in B grade")
else:
    print("You are in A grade.")