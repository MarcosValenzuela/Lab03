#This program will find the class grade

"""
start
create a list to store five numbers (float)
capture user's input five times for their grades
each time we caputre a user input, we apped the number to the list
sort the list ascending, then splice the items starting at index 2
once we have the three highest numbers we sum them then divide by 3
output a message to the user
end
"""

"""
create list

capture user input
append number to list

capture user input
append number to list

capture user input
append number to list

capture user input
append number to list

capture user input
append number to list

sort the list, then splice out to the lowest two numbers

output info to user

"""

grades = [] #list to hold the score

grade = input("Enter 1st grade: ")
grades.append(float(grade))

grade = input("Enter 2nd grade: ")
grades.append(float(grade))

grade = input("Enter 3rd grade: ")
grades.append(float(grade))

grade = input("Enter 4th grade: ")
grades.append(float(grade))

grade = input("Enter 5th grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]

grades = sum(grades)

result = grades/3

print("Average Grade {0:.2f}%".format(result))

