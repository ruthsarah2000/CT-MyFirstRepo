'''
You are provided with a Python script that uses conditional 
statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.
'''
number = int(input("Enter a number: "))    #added int so program allowed intergers to be entered by user


if number == 0:
    print("The number is zero.")   # moved to if statement
elif number % 2 == 0:              # added "=" and took out "!" to make statement calculate positive value
    print("The number is positive.")
else:
    print("The number is negative.")

'''
You are provided with a Python script that uses if-else structures for a story branching mechanism. 
There are some errors in the code. Identify and correct them.
 '''

choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")

'''
Harness the power of conditional statements to compare and determine values.

Task 1: Identify the Greatest
Write a Python program that prompts the user to enter three numbers. 
The program should then identify and print out the largest number among the three.

Task 2: Identify the Smallest
Extend your program from Task 1 to also determine the smallest number among the three and print it out.

Task 3: Equality Check
Enhance your program to handle cases where two or all of the numbers are equal. 
The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".
'''

number_1 = int(input("Input a number of your choice: "))
number_2 = int(input("Input a number of your choice: "))
number_3 = int(input("Input a number of your choice: "))

if number_1 == number_2:
    print("Your inputs are equal")
elif number_1 == number_2 == number_3:
    print("Your inputs are eqaul")
elif number_1 == number_3:
    print("Your numbers are equal")
else:
    print("Your inputs are not equal")

largest = max(number_1, number_2, number_3)

print("The largest number is: ", largest)

smallest = min(number_1, number_2, number_3)

print("The smallest number is: ", smallest)

'''
Task 1: Leap Year Checker
Write a Python program that prompts the user to input a year. The program should determine if the given year is a
leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every
year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these
centurial years are leap years if they are exactly divisible by 400.
Task 2: Century Verification
Add functionality to your program from Task 1 to inform the user if the entered year is a century year 
(e.g., 1900, 2000) regardless of whether it's a leap year or not.
Task 3: Time Traveler
Enhance your program to indicate if the provided year is in the future, past, or is the current year, compared to the
system's current year. You might find Python's datetime module helpful for this task.
'''


year = int(input("Enter desired year to be checked: " ))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year) )

# not divided by 100 means not a century year
# year divided by 4 is a leap year    
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

from datetime import datetime, timedelta
StartDay = datetime.today()
EndDay = StartDay + timedelta(90)
StartDate = StartDay.date()  
EndDate = EndDay.date()  
print(StartDate < EndDate)  




