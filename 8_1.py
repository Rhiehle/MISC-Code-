print("Task 0: ")
#task 0
def printFirst(mystring, x):
    print(mystring[:x])


printFirst('WGU College of IT', 3)
printFirst('WGU College of IT', 11)

print("\nTask 1: ")
#task 1
def printFirst(mystring, x):
    print(mystring[:x])


printFirst('WGU College of IT', 3)
printFirst('WGU College of IT', 11)

print("\nTask 2: ")
#Task 2
def getLast(mystring, x):
    x= int(len(mystring))-x
    return(mystring[x:])


print(getLast('WGU College of IT', 2))
print(getLast('WGU College of IT', 13))

print("\nTask 3: ")
#task 3
def containsWGU(mystring):
    if mystring.count("WGU") > 0:
        return True
    return False


print(containsWGU('WGU College of IT'))
print(containsWGU('Night Owls Rock'))

print("\nTask 4: ")
#task 4
def printWords(mystring):
    print(mystring.split())


printWords('WGU College of IT')
printWords('Night Owls Rock')

print("\nTask 5: ")
#task 5
def combineWords(words):
    white_space= " "
    words= white_space.join(words)
    return(words)


print(combineWords(['WGU', 'College', 'of', 'IT']))
print(combineWords(['Night', 'Owls', 'Rock']))

print("\nTask 6: ")
# Task 6
def replaceWGU(mystring):
    print(mystring.replace("WGU", "Western Governors University"))


replaceWGU('WGU Rocks')
replaceWGU('Hello, WGU')

print("\nTask 7: ")
#Task 7
# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
    # not working correctly
    new_mystring=mystring.split()
    if new_mystring[0] != "WGU":
        return mystring.replace("WGU", "")
    return mystring

print(removeWGU('WGU Rocks'))
print(removeWGU('Hello, WGUJohn'))

print("\nTask 8: ")
#Task 8
def removeSpaces(string1, string2):
    string1=string1.strip()
    string2=string2.strip()
    return string1+string2


print(removeSpaces('WGU Rocks    ', '  -You know it!'))
print(removeSpaces('Welcome WGU ', ' -IT Students'))

print("\nTask 9: ")
#Task 9
# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
    print( str(round(rate,2)))

# Student code goes here

# expected output: $34.79
displayHourlyRate(34.789123)

# expected output: $24.12
displayHourlyRate(24.123456)

print("\nTask 10: ")
#Task 10
# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
    counter=0
    for letter in mystring:
        if letter.isupper():
            counter=counter +1
    return(counter)


print(countUpper('Welcome to WGU'))
print(countUpper('Hello, Mary'))