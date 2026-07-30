# WAP to input users first name and print its leangh
A = input("Enter your name: ")
print("Length of name is:", len(A))

# WAP to find the occurance of '$' in a string
B = "I know i earn is $ and spend in $"
print("The occurance of a string: ", B.count("$"))

# Conditonal problems:

# 1. WAP to check if a number entered by the iser id odd or even:
num = int(input("Enter the number: "))
rem = num % 2

if (rem == 0 ):
    print("Even")
else:
    print("Odd")



# 2.WAP to find the greatest of 3 numbers entered by the user.
# it can give any kind of the largest value!


A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))

if (A >= B and A >= C):
    print("First is Largest:", A)
elif(B>= C):
    print("Second is Largest:", B)
else:
    print("Third is Largest:", C)
    

# FInd the largest number of 4:
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
D = int(input("Enter the fourth value: "))

if (A >= B and A >= C and A>=D):
    print("First is Largest: ", A)
elif(B>= C and B>=D):
    print("Second is Largest: ", B)
elif(C>=D):
    print("Third is Largest: ",C)
else:
    print("Fourt is Largest: ", D)


# 4. WAP to check if a number is a multiple of 7 or not:
thala = int(input("Enter the Number: "))

if (thala %7 ==0):
    print("This No. is Multiple of 7: ", thala)
else:
    print("It is not a multiple of 7")