# Indexing:
str = "Shivani mali"
ch = str[0]
print(ch)

# str[3] = "@"
# print(str[3]) 

str1 = "Shivani Mali"
print(str1[1 : 4])
print(str1[1 : 5])
print(str1[0 : 4])
print(str1[8 : 12])
print(str1[8 : ])   #for the last index you can use the nothing becasue py can understand
print(str1[8 : len(str1)])

str2 = "I can do it!"
print(str2[:4])  #[0:4]
print(str2[5:])  #[5: ending_indx]

# Negative index:
stre = "Apple"
print(stre[-5 : -2])
print(stre[-3 : -1])
print(stre[-5 :])

