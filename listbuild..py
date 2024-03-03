'''
You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.
Task 1: Given the list of grades: Sort the grades in descending order and display the sorted list.
'''

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades)

'''
Task 2: Calculate the average grade and display it.
'''
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average = ((85+90+78+88+76+95+89+80+72+93)/10)

print(average)

'''
Task 3: Replace any grade below 80 with the value Failed.
'''
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

for i in range (len(grades)):
    if grades [i] < 80:
        grades [i] = "FAIL"
print(grades)

'''
You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains 
the names of students who attended the last class.
'''
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted_attended = set (submitted) & set (attended)

print("Students who submitted assignments and attended class: ")
print(submitted_attended)

'''
Task 2: Check if the two lists are identical in terms of their content, regardless of order.
'''
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if set(submitted ) == set(attended):
    print("The list is identical")
else:
    print("The list is not identical")

'''
You have a list of daily temperatures for a month, and you'd like to extract specific data from it.
Task 1: Given the list of temperatures: Extract the temperatures for the second week (7 days) of the month.
'''
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures[7:14]
print(second_week)

'''
Task 2: Extract all the temperatures above 100.
'''
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
for num in temperatures:
    if num > 100:
        print(num)

'''
 Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
'''
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
reversed_list = temperatures [::-1]
print(reversed_list)
fifth_tenth = temperatures[4:10]
print(fifth_tenth)

'''
The aim of this assignment is to practice using list comprehensions and membership operators in Python.
You have a list of numbers, and you'd like to generate a new list based on certain conditions.
Given the list: Use a list comprehension to create a new list containing only even numbers.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)

'''
Task 2: Use a list comprehension to create a new list containing numbers greater than 5.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num > 5:
        print(num)

'''
Task 3: Check if the number 7 is in the original numbers list.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 7 == 0:
        num = "Yes, the number 7 is in this list."
        print(num)

'''
The aim of this assignment is to integrate various list operations and methods to solve a complex problem.
You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.
Given the lists: 
Create a new list where each element is a dictionary with keys name, grade, and activity and the corresponding values from the provided lists.
'''
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]      

new_list = [{"name": name, "grade": grade, "activity": activity} for name, grade, activity in zip(students, grades, activities)]

print(new_list)

'''
Task 2: Filter out students who have grades below 80.
'''
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
grade_list = [{"name": name, "grade": grade,} for name, grade, in zip(students, grades,) if grade <= 80] 

print(grade_list)

'''
For the remaining students, add a new key-value pair in their dictionary: "status": "Passed".
'''
pass_list = [{"name": name, "grade": grade, "status": "Passed"} for name, grade, status in zip(students, grades, "Passed") if grade > 80] 
print(pass_list)
