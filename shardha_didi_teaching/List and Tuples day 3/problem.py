# # 1. WAP to ask the user to enter names of their 3 favourite mocies and store then in a list
# A = input("Enter the first movie name: ")
# B = input("Enter the Second movie name: ")
# C = input("Enter the Third movie name: ")
# list = [A , B, C]
# print("here is your list: \n", list )


# # or
# Movies = []
# A = input("Enter the first movie name: ")
# B = input("Enter the Second movie name: ")
# C = input("Enter the Third movie name: ")

# Movies.append(A)
# Movies.append(B)
# Movies.append(C)

# print(Movies)



# Question 2. WAP to check is a list contains a palindrome of elements.
list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    ("Not a palindrome")


# WAP to count the no. of students with the "A" grade in the follwoing tuple:
# Given tuple is ["C", "D", "A", "A", "A", "B", "B", "A"]

Grades = ["C", "D", "A", "A", "A", "B", "B", "A"]

print("Total A grades are: ", Grades.count("A"))


# store and sort list them from A to D:
tum = ["C", "D", "A", "A", "A", "B", "B", "A"]
print(tum)
tum.sort()
print(tum)



