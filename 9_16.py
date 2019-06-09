#9.16 Lists and dictionaries practice
#Task 0
print("\nTask 0: ")


# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    print(mystring[:x])
# Student code goes here

# expected output: WGU
printFirst('WGU College of IT', 3)

# expected output: WGU College
printFirst('WGU College of IT', 11)

#task 1
print("\nTask 1: ")
# Complete the function to return the first two items in the given list
def getFirstTwo(mylist):
    return(mylist [:2])


print(getFirstTwo([8, 3, 5, 2, 10]))
print(getFirstTwo([15, 2, 10, 12]))

#task 2
print("\nTask 2: ")


# Complete the function to return the last two items in the given list
def getLastTwo(mylist):
    mylist_len=len(mylist)
    mylist_len=mylist_len-2
    return mylist[mylist_len:]


print(getLastTwo([8, 3, 5, 2, 10]))
print(getLastTwo([15, 2, 9, 12]))

#task 3
print("\nTask 3: ")
# Complete the function to add num1 to the end of the given list
def addToEnd(mylist, num1):
    mylist.append(num1)
    return mylist


print(addToEnd([4, 5, 6], 7))
print(addToEnd([9, 8, 7], 6))

#task 4:
print("\nTask 4: ")


# Complete the function to add num2 to the front of the given list
def addToFront(mylist, num1):
    mylist.insert(0,num1)
    return mylist


print(addToFront([4, 5, 6], 3))
print(addToFront([9, 8, 7], 10))

#Task 5:
print("\nTask 5: ")
# Complete the function to return a new list containing
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
    first_two= mylist[:2]
    len_of_list= len(mylist)-2
    last_two=mylist[len_of_list:]
    return first_two+last_two


print(getFirstTwoAndLastTwo([8, 3, 7, 15, 2, 10, 19, 1]))
print(getFirstTwoAndLastTwo([7, 15, 2, 10, 19, 1, 3, 5]))

#Task 6:
print("\nTask 6: ")
# Complete the function to remove the first item in the given list
def removeFirst(mylist):
    mylist.remove(mylist[0])
    return mylist


print(removeFirst([6, 7, 8, 9]))
print(removeFirst([1, 2, 3, 4]))

#Task 7:
print("\nTask 7:")
# Complete the function to remove the third item in the given list
def removeThird(mylist):
    mylist.remove(mylist[2])
    return mylist


print(removeThird([6, 7, 8, 9]))
print(removeThird([1, 2, 3, 4]))


#task 8:
print("\nTask 8: ")
# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
    if ascending is True:
        mylist.sort()
        return mylist
    mylist.sort(reverse=True)
    return mylist


print(sortList([19, 4, 33, 12], True))
print(sortList([19, 4, 33, 12], False))

#task 9
print("\nTask 9: ")
# Complete the function to return a dictionary using
# list1 as the keys and list2 as the values
def createDict(list1, list2):
    i=0
    new_dic={}
    for list in list1:
        new_dic[list1[i]]=list2[i]
        i=i+1
    return new_dic



# Student code goes here

# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}
print(createDict(['tomato', 'banana', 'lime'], ['red', 'yellow', 'green']))

# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia', 'Dublin', 'Jakarta']))

#task 10
print("\nTask 10: ")

# Complete the function to return a dictionary value
# if it exists or return Not Found if it doesn't exist
def findDictItem(mydict, key):
    if key in mydict:
        return mydict[key]
    return "Not Found"


print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}, 'banana'))
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))

#task 11
print("\nTask 11: ")
# Complete the function to remove a dictionary item if it exists
def removeDictItem(mydict, key):
    if key in mydict:
        del mydict[key]
    return mydict



print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}, 'banana'))
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))

#task 12
print("\nTask 12: ")


# Complete the function to print every key and value
def printDict(mydict):
    for key, value in mydict.items():
        print(key,"=",value)

# Student code goes here

# expected output:
#        tomato=red
#        banana=yellow
#        lime=green
printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})

# expected output:
#        Brazil=Brasilia
#        Ireland=Dublin
#        Indonesia=Jakarta
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})