# ---- Math Module --- ##
import math

#task 1
print("Task 1:")
# use the math module to determine the factorial of the number 7 and print the result
# expected outcome: 5040
print(math.factorial(7))

#task 2
print("\nTask 2:")
# use the math module to determine the square root of the number 27 and print the result
# expected outcome: 5.196152422706632
print(math.sqrt(27))

#task 3
print("\nTask 3")
# use the math module to determine the largest integer less than or equal to 15.87 and print the result
# expected outcome: 15
print(math.floor(15.87))

#Task 4
print("\nTask 4:")
# use the math module to determine the smallest integer integer greater than or equal to 15.87 and print the result
# expected outcome: 16
print(math.ceil((15.87)))

#Task 5
print("\nTask 5:")
# use the math module to determine e to the power of 4
# expected outcome: 54.598150033144236
print(math.e**4)


print("\nRandom Module\n")
#Task 1
print("Task 1:")
## ---- Random Module --- ##
import random

# use the random module to print a random integer between 2 and 20, exclusive
print(random.randrange(2,20))
#Task 2
print("\nTask 2:")
# use the random module to print a random number from the range 1 to 100, inclusive
print(random.randint(1,100))

#Task 3
print("\nTask 3")
# use the random module to return a random floating point number
x=random.random
print(x)

#Task4
print("\nTask 4: ")
# Create a list of 6 words. Then use the random module to return a random element from that list.
list_six_words=["to","be","or","not","too","bee"]
#Yes I spelt it wrong

print(random.choice(list_six_words))

print("\nOs Module...Joy\n")

## ---- OS Module --- ##
import os
#Task 1
print("Task 1: ")
# use the os module to create a hard link to C://myfile.txt at C://myPython/myfile.txt

path = "/C://myPython/myfile.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

os.close( fd )

dst = "C://myfile.txt "
os.link( path, dst)

# use the os module to delete the file C://myfile.txt


# use the os module to return the current working directory


# use the os module to change the root directory to C://home/


print("\nDatetime Module\n")
## ---- Datetime Module --- ##
import datetime
#Task 1
print("Task 1: ")
# use the datetime module to print the current year
print(datetime.datetime.now().year)

#Task 2:
print("\nTask 2:")
# use the datetime module to print the current month
print(datetime.datetime.now().month)

#Task 3:
print("\nTask 3:")
# use the datetime module to print the current day
print(datetime.datetime.now().day)

#task 4
print("\nTask 4:")
# use the datetime module to print the total number of seconds in 4 days
# expected outcome: 345600.0
print (datetime.timedelta(4).total_seconds())

#task 5
print("\nTask 5:")
# print today's date one year from now
print(datetime.datetime.today().date() + datetime.timedelta(days=365))

print("\nLookup stuff\n")
## ---- Lookup  --- ##
# You need to use the datetime library to account for time zone adjustments, but aren't sure which method(s) to use.
# You are taking an exam and can't google it. What Python function will allow you to look up and locate the method?
# Write your code below:

#help(datetime)