# List = [] use to store the values , and diffrent types of DT are used
# list are -= mutable(Chnagble)


Marks = [32, 32.3, 56.90, 45.1, 99.34]
print(Marks)
print(type(Marks))


# we kind fin like indexing used in the string:
print(Marks[0])
print(len(Marks))

# YOu can store any type of data over here in a single list perfeclty and peoperly!
Student = ["Karan,", 23, "90%"]
# print(Student [0])
Student[0] = "arjun"
print(Student)
# print(Student[4]) out of the range


# Slicing in List and give the sublist over here:
marks = [85, 94, 76, 63, 48]
print(marks[:4])
print(marks[0:])
print(marks[2:4])

# the -ve slicing is also you can do:
print(marks[-5:-2])

# list method:

list = [1, 2, 3, 4, 5]
list.append(4)
print(list)

# orders ascending- {012---} and decending {210-1---}: it is used in sorting 

list1= ["banana", "apple", 'guava', 'orange', "graphes"]
print(list1.sort(reverse = True))
print(list1.sort()) # it give the null values!!!
print(list1)


# Reverse the values
list1.reverse()
print(list1)

# Insert the values: change the index values:
lolo = [2, 1, 3]
lolo.insert(9,5)
print(lolo)

