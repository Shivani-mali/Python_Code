# age = int(input("Enter your age: "))
age = 19

if(age >= 18):
    print("you are Eligible for voting and apply for licens")
    print("Can drive")
    print("can vote")
else:
    print("Not eligible ")


light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("look")
else:
    print("Nothing is shown")

#  if alwys check condition and elif 
num =5

if (num > 2):
    print("greater than 2")
elif(num>3):
    print("greater than 2")

# and evrything wrong then we go within the else last chosice 
# Grade system question:

# Marks = float(input("Enter your marks:"))

# if (Marks >= 90):
#     print("your Grade is 'A' ")
# elif(Marks>=80 and Marks< 90):
#     print("your grade is 'B' ")
# elif(Marks>=70 and Marks< 80):
#     print("your grade is 'C' ")
# else:
#     print("your grade is 'D' ")

# print("Grade of the student is ==>> ", Marks)



Marks = float(input("Enter your marks:"))

if (Marks >= 90):
    grade = "A"
elif(Marks>=80 and Marks< 90):
    grade = "B"

elif(Marks>=70 and Marks< 80):
    grade = "C"

else:
    grade = "D"

print("Grade of the student is ==>> ", grade)



# Nesting COndition:
age =34

if(age>= 18):
    if(age >= 80):
        print("\nCannot drive")
    else:
        print("\nCan drive! ")
else:
    print("\nCannot Drive...")