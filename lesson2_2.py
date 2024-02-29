'''
You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. 
Identify and fix them.
'''

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": # Corrected this line, added double equals sign for comparison
        print("You found a bird's nest!")
    else:
        print("You found a boat!") 
elif place == "cave": # Changed elif to else if
    print("You find a hidden treasure!")
else:
    print("Sorry, your selection is not valid.")

'''
Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to 
"light a torch" or "proceed in the dark", and provide outcomes for each decision.
'''
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark? ")
    if cave_action == "light a torch":
        print("Smart, you like to plan for surprises.")
    else:
        print("You are a thrill seeker!")
    if cave_action not in ["light a torch", "proceed in the dark"]:
        print("Try again. Please enter either 'light a torch' or 'proceed in the dark'.")
else:
    print("Invalid choice. Please choose either 'forest' or 'cave'.")

'''If the user makes an invalid choice at any point, use the pass statement for now. 
Later, you can enhance this to provide feedback or a different branch of the story.
'''
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  # Invalid action in the forest
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark? ")
    if cave_action == "light a torch":
        print("Smart, you like to plan for surprises.")
    elif cave_action == "proceed in the dark":
        print("You are a thrill seeker!")
    else:
        pass  # Invalid action in the cave
else:
    print("Invalid choice. Please choose either 'forest' or 'cave'.")

'''
You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
'''
attendees = int(input("Enter number of attendees: ")) # add int to variable for user input
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


'''
Based on the corrected code from Task 1, further enhance the program to recommend additional facilities 
like "audio system" or "projector" based on the number of attendees.
'''

attendees = int(input("Enter number of attendees: "))  # Convert input to integer
venue = "large hall" if attendees > 100 else "conference room"
print("Venue:", venue)

venue_option = input("Would you like to add an audio system (for less than 100 attendees) or a projector (for more than 100 attendees)? ")

if venue_option == "audio system" and attendees < 100:
    print("You've selected to add an audio system.")
elif venue_option == "projector" and attendees > 100:
    print("You've selected to add a projector.")
else:
    print("Invalid choice or mismatch between attendees and equipment. Please review your selection.")

'''
Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
'''
attendees = int(input("Enter number of attendees: "))  # Convert input to integer
venue = "large hall" if attendees > 100 else "conference room"
print("Venue:", venue)

venue_option = input("Would you like to add an audio system (for less than 100 attendees) or a projector (for more than 100 attendees)? ")

if venue_option == "audio system" and attendees < 100:
    print("You've selected to add an audio system.")
elif venue_option == "projector" and attendees > 100:
    print("You've selected to add a projector.")
else:
    print("Invalid choice or mismatch between attendees and equipment. Please review your selection.")

food_option = input("Would you like vegetarian food? (Y/N) ")
if food_option == "Y":
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")

'''
You are provided with a Python script that is supposed to handle errors silently, but it has some mistakes. Identify and fix them.
'''

try:
    x = 1 / 0
except ZeroDivisionError: # added colon to close 
    pass

'''
Based on the corrected code from Task 1, enhance the program to handle other potential errors, 
such as ValueError when trying to divide a number by a string.
'''
try:
    x = 1 / 0
except ZeroDivisionError:
    pass
try:
    num = int('123') # the number should be 123 
except ValueError:
    pass

'''
Ask the user for a filename to read. Try to open and read the file. 
If the file doesn't exist, use the pass statement to handle the error silently.
'''

try:
    x = 1 / 0
except ZeroDivisionError:
    pass
try:
    num = int('123') 
except ValueError: 
    pass
try:
    file_name = input("Print filename to read file: ")
except ValueError:
    pass # place holder to add file names for users to read

'''
You are provided with a Python script that is supposed to assist in shopping, but it has errors. Identify and fix them.
'''
weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

'''
Based on the corrected code from Task 1, further enhance the program to recommend additional 
items like "hat" or "boots" based on the weather.
'''
weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

if clothing == "umbrella":
    print("Boots are a must!")
elif clothing == "sweater":
    print("A hat will also be required.")

'''
Based on the clothing recommendation, suggest an accessory. For instance, if "sunglasses" were recommended, suggest "sunscreen" 
as an accessory.
'''

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

if clothing == "umbrella":
    print("Boots are a must!")
elif clothing == "sweater":
    print("A hat is also required.")
else:
    print("I recommend sun screen!")

'''
You are provided with a Python script that is supposed to monitor system parameters, but it has some mistakes. Identify and fix them.
'''

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90: # missing colon after 90
    pass

'''
Based on the corrected code from Task 1, enhance the program to also monitor memory usage and disk space, 
and provide alerts accordingly.
'''
import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_usage = random.randint(0, 100)

if cpu_usage > 80:
    print("High CPU usage!")
elif cpu_usage > 90:
    pass

if memory_usage > 70:
    print("Low on available memory")
elif memory_usage > 90:
    print("It's time to save to an external drive")

if disk_usage > 50:
    print("Moderate space usage")
elif disk_usage > 90:
    print("High disk space usage")

'''
If any of the system parameters exceed a certain threshold, print an alert message. However, if the system parameter 
is within a "gray zone", use the pass statement to silently log this without alerting the user.
'''
import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_usage = random.randint(0, 100)

if cpu_usage > 80:
    print("High CPU usage!")
elif cpu_usage > 90:
    pass

if memory_usage > 70:
    print("Low on available memory")
elif memory_usage > 90:
    print("It's time to save to an external drive")

if disk_usage > 50:
    print("Moderate space usage")
elif disk_usage > 90:
    print("High disk space usage")

if cpu_usage > 99 or memory_usage > 99 or disk_usage > 99:
    print("At capacity, address immediately!")
elif 95 < cpu_usage <= 98 or 95 < memory_usage <= 98 or 95 < disk_usage <= 98:
    pass
