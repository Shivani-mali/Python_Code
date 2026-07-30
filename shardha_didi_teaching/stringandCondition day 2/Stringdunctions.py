# String Functions:
# 1. endwith("..")
str = 'i am a Coder'
print(str.endswith("er"))
print(str.endswith("wew"))

# 2. capitalize()
# it capitalize the value of 1sr letter give string:
print(str.capitalize())
print(str)

# 3. replace(old,new)
str1 = "i am person, i dont know whom is he?"
print(str1.replace("person", "Animal"))

# 4. find(word) use to get the 1st occurance 1st letter get
str2 = "I am an Engineer, Who loves coding"
print(str2.find("e")) #it give index number of his letter
print(str2.find("am")) #it give index number of his letter


# 5. count("") used for count the occrences of substr
print(str2.count("o"))
