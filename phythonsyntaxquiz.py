#Question 1
#Task 1
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#Task 2
response = "happy"
if response == "happy":
    print("I hope your day gets better!")
else:
    print("I hope your day gets better!")

#Task 3
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")

#Question 2
#Task 1
# Python, oh Python, so clear and so neat
# With every new challenge, you're hard to beat.
# I cant wait to see what is your next treat!
# The road may be rocky, but no need to despair,
# Errors are spotted by syntax in the clear.
# Stay the course, your reward is near. 
    
#Task 2
'''
Python, in the realm of code you shine,
With simplicity and grace, you're truly divine.
I am having a blast figuring you out,
The nooks and crannies are all figured out.
Python, oh Python, 
In the world of coding, you have me be dazzled.
'''
#Task 3
# This is a line from my first poem
# The road may be rocky, but no need to despair,
# This is a line from my second poem
'''
The nooks and crannies are all figured out.
'''

#Question 3
#Task 1
pi_value = 3.14
user_age = 25
user_location = "New York"
max_limit = 1000

#Question 4
#Task 1
variable_a = "Hello, World!" # This is a string
variable_b = 23 # This is an interger
variable_c = 3.14 # This is a float
variable_d = True # This is a boolean
print(variable_a, type(variable_a))
print(variable_b, type(variable_b))
print(variable_c, type(variable_c))
print(variable_d, type(variable_d))

#Question 5
#Task 1
dynamic_variable = "This is a string"
dynamic_type = type(dynamic_variable)
print(dynamic_type)

dynamic_variable = 100
dynamic_type = type(dynamic_variable)
print(dynamic_type)

dynamic_variable = 25.5
dynamic_type = type(dynamic_variable)
print(dynamic_type)

#Question 6
#Task 1
item_cost_egg = 3.99
item_cost_bread = 5
item_cost_milk = 7.99
total_cost_egg_bread_milk = item_cost_egg + item_cost_bread + item_cost_milk
print(total_cost_egg_bread_milk)

#Task 2
savings_acct = 20000
year = 1
int = 2.9
future_sav = savings_acct * (( 1 + (.01 * int)) ** year) # .01 is rounding the value to 2 decimal places
print(future_sav)

#Task 3
length_rec = 20
width_rec = 7
area = length_rec * width_rec
perimeter = 2*(length_rec+width_rec)
print(area)
print(perimeter)

#Question 7
#Task 1
x = 100
y = 15
x, y = y, x
print("Value of x:", x)
print("Value of y:", y)

#Task 2
num = 100
sqrt_num = num ** 0.5
print(sqrt_num)
if sqrt_num != "float":
    print("The number is a perfect square")
else:
    print("The number is not a perfect square")

#Question 8
#Task1 - Determine when to charge my cell phone
batt_charge_below_50 = False
going_out = True
charge_cell = going_out and batt_charge_below_50
print(charge_cell)

#Task 2
x = 10
y = 15
z = 20
calc_values = x * y - z
print(calc_values)   
Calc_values = (x * y - z)
print(Calc_values)

#Task 3
x = 6
y = 15
z = 5
comparison_logic = x + z < y > z
print(comparison_logic)
