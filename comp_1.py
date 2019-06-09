#Task 1
# create a function with receives two integers as input, adds them and returns the sum
def does_basic_math(int1,int2):
    return int1+int2

# run your function and print the result with integers 7 and 9
# expected outcome: 16
print(does_basic_math(7,9))

# run your function and print the result with integers 20 and 49
# expected outcome: 69
print(does_basic_math(20,49))
# Run your function with integers 2 and 8, and save the output to a new variable called myNewSum. Print myNewSum.
# expected outcome: 10

myNewSum=does_basic_math(2,8)
print(myNewSum)

# You are provided a student's score on the recent exam.
# Create a function that will print a reply based on the score.
# Students who score 90 points or more receive an A and pass the course.
# Students receiving 80 points or more receive a B and pass the course.
# Students receiving 79 points do not pass and need to retake the exam.
# Students receiving a score of 0 have not attempted the exam and need instructions to schedule.

def grade_report(test_result):
    if test_result >= 90:
        return ("receive an A and pass the course.")
    if test_result < 90 and test_result >= 80:
        return("80 points or more receive a B and pass the course.")
    if test_result < 80 and test_result != 0:
        return("did not pass and need to retake the exam.")
    if test_result==0:
        return("Did not attempted the exam and need instructions to schedule.")


# Run the function with a score of 90 and print the result
# expected outcome: You received an A and have passed the course.
print(grade_report(90))

# Run the function with a score of 70 and print the result
# expected outcome: You have not passed the course. Please retake the exam.
print(grade_report(70))


# use the range method to print out numbers 6-12
print(list(range(6,13)))


# create a list containing the names Dana, Connie, Jessica, Mike, and Dana
name_list= ['Dana', 'Connie', 'Jessica', 'Mike', 'Dana']


# Print the length of the list.
# expected outcome: 5
print(len(name_list))


# Check to see if Candice is in the list. If not in the list, add her and print the list.
# expected outcome: ['Dana', 'Connie', 'Jessica', 'Mike', 'Dana', 'Candice']
for names in name_list:
    if names!="Candice":
        name_list.append("Candice")




# Create and print a single string containing all of the names separated by commas
# expected outcome: Dana, Connie, Jessica, Mike, Dana, Candice
print("Dana, Connie, Jessica, Mike, Dana, Candice")



# Print only the names Dana and Mike from myNames
# expected outcome: ["Mike","Dana"]



# ensure that each name is only listed once and print the list of unique values
# expected outcome: ['Dana', 'Connie', 'Jessica', 'Mike', 'Candice'] *note: order of items in list may vary



# create an individual message for each unique name and welcome them to WGU
# expected outcome: Welcome to WGU, Dana
#                   Welcome to WGU, Jessica
#                   Welcome to WGU, Mike
#                   Welcome to WGU, Candice
#                   Welcome to WGU, Connie

i=0

while i < 5:
    print("Welcome to WGU, "+name_list[i])
    i=i+1
