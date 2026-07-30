#Exercise 2:!
# Excersice 2: Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
#  Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime



import time

timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))  # Convert hour to an integer
print(hour)

if 0 <= hour < 12:
    print("Good morning sir!")
elif 12 <= hour < 17:
    print("Good afternoon sir!")
else:
    print("Good night sir!")
