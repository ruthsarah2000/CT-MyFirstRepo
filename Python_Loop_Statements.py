'''
The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.
Task 1: Code Correction
The range() function is used to generate a sequence of numbers. However, the code snippet provided below does not work as intended. 
Your task is to identify why the loop might not be executing and correct the code so that it prints numbers from 5 down to 3.
'''
for i in range(5, 2, -1):       # -1 to indicate end of list 
    print(i)

'''
Task 2: Your Mood Today
Write a program that simulates different moods for each day of the week. Create a list of moods such as
"Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and
for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of
the random module to select the mood.
'''
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursady", "Friday", "Saturday"]

for day in days_of_the_week:
    random_mood = random.choice(moods)
    print(f"On {day}. I feel {random_mood}")

'''
Task 3: Going Backwards
Create a countdown timer that starts from 10 and counts down to 1. Use the range() function to generate the countdown sequence. 
Each number should be printed on a new line. This task will help you understand how to generate a decreasing sequence with range().
'''

for i in range (10, 0, -1):
    print(i)

'''
Objective:
The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop code snippet, 
simulate a mood tracker, and generate a multiplication table.
Task 1: Code Correction
The code below is intended to print a 3x3 grid of asterisks. However, the current output is not as expected. 
Identify the logical errors in the nested loops and correct the code so that it prints the grid correctly, with each row of asterisks on a new line.
'''
for i in range(3):
    for j in range(3):
        print("*", end=" ")    # end= " " to print asterisks horizontally
    print()                    # stops code

'''
Task 2: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner 
loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.
'''
import random

mood = ["Happy", "sad", "calm", "angry", "excited"]
day_of_week = ["Sundays", "Mondays", "Tuesdays", "Wednesdays", "Thursdays", "Fridays", "Saturdays"]
time_of_day = ["morning", "afternoon", "evening"]

for day in day_of_week:
     print(f"{day}:")
for time in time_of_day:
        random_mood = random.choice(mood)
        print(f"{time}: {random_mood}")
        print()


'''
Task 3: Multiplication Table
Your task is to create a multiplication table for numbers 1 through 5. Use nested loops where the outer loop represents 
the multiplier and the inner loop represents the multiplicand. Print the results in a tabular format.
'''

multiplier = [1, 2, 3, 4, 5]
multiplicand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for multiplier in range (1, 6):
    print(f"Multiplication Table for {multiplier}")
    for multiplicand in range (1, 13):
        result = multiplier * multiplicand
        print(f"{multiplier} * {multiplicand} = {result}")
        print()

'''
Objective:
The aim of this assignment is to explore and practice the control statements within Python's for loop, such as break, continue, pass, 
and the else clause. You will correct a loop, simulate mood swings with loop control, and implement a search with an else clause.
Task 1: Code Correction
The loop below is meant to print all numbers from 1 to 10, but it stops prematurely due to a break statement. 
Correct the code so that it skips over the number 5 and continues to print the rest of the numbers.
'''
for i in range(1, 11):
    if i == 5:
        continue  # change break to continue
    print(i)

'''
Task 2: Your Mood Swings
Write a program that represents your mood swings throughout a day. The program should loop over each hour of the day and assign a random 
mood from a list for each hour. However, at 'lunchtime' (which you can define as a specific hour), the program should not print the mood. 
Use the continue statement to achieve this behavior.
'''
import random

mood = ["Happy", "Sad", "Excited", "Angry", "Anxious", "Nervous", "Calm", "Emotional", "Crazy", "Drained"]
hour_of_day = ["0100", "0200", "0300", "0400", "0500", "0600", "0700", "0800", "0900", "1000", "1100", "midday", "1300", "1400", "1500", "1600", "1700", "1800", "1900", "2000", "2100", "2200", "2300", "midnight"]
lunch_time = "midday"

for hour in hour_of_day:
    if hour == lunch_time:
        continue
    random_mood = random.choice(mood)
    print(f"At {hour}. I usually feel {random_mood}")
    print()

'''
Task 3: The Persistent Loop
Implement a for loop that searches for a specific number in a list of numbers. If the number is found, use break to exit the loop. 
If the loop completes without finding the number, an else clause should be used to print a message stating that the number was not found. 
This task will help you understand how to use the else clause in conjunction with the break statement in loops.
'''
    
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5, 16, 17, 18, 19, 20]
target = 35

for num in list:
    if num == 35:
        print(f"We found {target} in the list")
        break
    else:
        print(f"{target} was not found in this list")
        break

'''
Objective:
The aim of this assignment is to understand the impact of increment placement within a while loop in Python. 
You will experiment with different placements of the increment operation and observe how it affects the loop's execution and logic.
Task 1: Increment at the Start
Given the following code snippet, predict the output and then run the code to verify your prediction. 
Explain why the output is what it is based on the placement of the increment operation.
'''
marshmallows = 0   # starting point of zero for adding marshmallows
while marshmallows < 5: # range of adding marshmallows
    marshmallows += 1   # increment operation
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
# the output is adding incrementally to each scenario from 0 to 5 based on line 9 marshmellows to start is zero and line 10 while scenario is 
# range between 1 and 5
    
'''
Modify the code from Task 1 by moving the increment operation to the end of the loop. Predict what the output will be and then run 
the code to check your prediction. Discuss the differences in the output and how the placement of the increment affects the loop's behavior.
'''
marshmallows = 0   
print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
while marshmallows < 5: 
    marshmallows += 1  
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
# The sequence of operation changed but the output remains the same 
    
'''
Task 3: Off-by-One Error Investigation
Create a while loop where an off-by-one error could occur due to the placement of the increment operation. Your loop should aim to fill a 
bag with exactly 10 marshmallows, but due to the off-by-one error, it either has too few or too many. Correct the error and explain the 
importance of increment placement in preventing such errors.
'''
marshmallows = 1   
while marshmallows < 8: # incorrect range to get to 10 marshmallows
    marshmallows += 1   # increment operation
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows in the bag.")

'''
Correct increment to get to 10 marshmallows in the bag
'''
marshmallows = 1   
while marshmallows < 10: # correct range to get to 10 marshmallows in the bag
    marshmallows += 1   
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows in the bag.")

'''
The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different 
conditions to see how they influence the behavior of the loop.
Task 1: Loop Condition Exploration
Write a while loop with a condition that will never be true (an infinite loop). Inside the loop, print a statement. 
Then, use a break statement to exit the loop after 5 iterations. Explain the role of the loop condition and the break statement in 
controlling the loop execution.
'''
iteration = 0

while True:  # This condition will always be true, creating an infinite loop
    print("I am printing continuously.")
    iteration += 1
    if iteration >= 5:
        break  # Exit the loop after 5 iterations

'''
Task 2: Conditional Exit
Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. 
The loop should terminate naturally once the condition is met. Discuss how the loop condition determines when the loop exits.
'''

iteration = 0

while iteration < 5: # removing the true allows the loop to cycle through to a condition that will close the llop
    print("I am going to stop printing eventually .")
    iteration += 1 # with the loop broken, no 'break' is needed

'''
Task 3: Loop with Multiple Conditions
Create a while loop that continues to run as long as multiple conditions are true. Use the and or or operators to combine conditions. 
Describe how combining conditions can create more complex loop behaviors.
'''

tunnel = [False, False, True, False]
index = 0

while index < len(tunnel) and not tunnel[index]:
    print("Keep going through the tunnel")
    index += 1

'''
Objective:
The aim of this assignment is to master the use of else, break, continue, and pass in conjunction with while loops. 
You will implement loops that utilize these control statements to manage loop execution flow.
Task 1: Using else with while
Write a while loop that attempts to find a specific value in a list. Use an else clause to print a message if the value is not found. 
Explain how the else clause works with the while loop.
'''
master_list = [3, 6, 7, 17, 25, 33, 47, 51, 59, 67, 73]
target = 10

found = False 
index = 0

while index < len(master_list):
    if master_list == target:
        found = True
        print(f"Found {target} at index {index} in the list.")
        break
    index += 1
else:
    print(f"The number {target} was not found in this list.")

'''
Task 2: Loop Interruption with break
Create a while loop that runs indefinitely, printing out the current time. Use a break statement to exit the loop if a certain condition 
is met (e.g., if the current time matches a target time). Discuss how the break statement can be used to exit a loop based on a condition.
'''

import datetime

# Define the target time
target_time = datetime.time(12, 30)  # Example: 12:30 PM

# Start the while loop
while True:
    current_time = datetime.datetime.now().time()  # Get the current time
    print(f"Current time: {current_time}")
    
    # Check if the current time matches the target time
    if current_time.hour == target_time.hour and current_time.minute == target_time.minute:
        print("Target time reached. Exiting the loop.")
        break  # Exit the loop if the target time is reached

'''
Task 3: Skipping Iterations with continue
Develop a while loop that iterates over a range of numbers. Use the continue statement to skip over specific numbers 
(e.g., multiples of 3) and print the rest. Explain the purpose of the continue statement and how it affects the loop's iteration.
'''
# Set the range of numbers
start = 1
end = 10

# Start the while loop
current_number = start
while current_number <= end:
    # Check if the current number is a multiple of 3
    if current_number % 3 == 0:
        # Skip over multiples of 3 using continue statement
        current_number += 1
        continue
    
    # Print the current number if it's not a multiple of 3
    print(current_number)
    
    # Move to the next number
    current_number += 1

'''
Task 4: The Placeholder pass
Implement a while loop where you want to temporarily skip the implementation of a condition but plan to add more code later. 
Use the pass statement as a placeholder. Describe the use of pass in a loop and when it might be useful.
'''
while True:
    pass # placeholder condition for use at another time. 

'''
Objective:
The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness 
into your programs. You will simulate a dice-rolling game and extend it to include more complex game mechanics.
Task 1: Dice Rolling Simulator
Using the provided code snippet, simulate rolling a six-sided die 10 times. Extend the simulation to keep track of how many times each number 
is rolled. After the simulation, print out the frequency of each number.
'''
import random

# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")

'''
Task 2: Random Choice Game
Create a game where a player has to guess the random item picked by the computer from a list. Use random.choice() to select the 
item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
'''

import random
number = random.randint(1, 25)

guess = int(input("Guess the number between 1 and 25): "))

if guess == number:
    print("You guessed the correct number!")
else:
    print("Sorry, you guessed the worng number, the correct nummber was:", number)

'''
Task 3: Shuffling a Deck
Simulate shuffling a deck of cards using random.shuffle(). Create a list representing a deck of cards, then shuffle it and 
print the shuffled deck. Discuss how random.shuffle() can be used in game development or other applications.
'''
import random 

# Create a list representing a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Print the shuffled deck
print("Shuffled deck:")
for card in deck:
    print(card)

'''
The Random Challenge Course
The aim of this assignment is to challenge your understanding of the random package by creating a series of mini-games that require 
different aspects of randomness. You will create three mini-games, each focusing on a different function from the random package.
Task 1: The Guessing Game
Implement a number guessing game where the computer randomly selects a number within a range, and the player has to guess it. 
Use random.randint() to generate the number and give the player a hint after each incorrect guess whether their guess was too high or too low.
'''
import random

def number_bank(start, end):
    
    secret_number = random.randint(start, end)
    
    print(f"Welcome to the Number Guessing Game! Guess a number between {start} and {end}.")
    
    while True:
        
        guess = int(input("Enter your guess: "))
        
     
        if guess == secret_number:
            print("Congratulations! You've guessed the correct number.")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

start_range = 0
end_range = 47


number_bank(start_range, end_range)

'''
Task 2: The Magic 8-Ball
Create a Magic 8-Ball program that provides random advice. Use random.choice() to select a random response from a list of 
possible answers every time the user asks a question.
'''
import random

def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Yes",
        "Absoluterly not.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "You are correct",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "Is that a real question?",
        "You should consider asking better questions.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "That is a bad idea."
    ]

    print("Welcome to the cyber Magic 8-Ball! Ask me a question.")
    while True:
        user_question = input("Enter your question (or type 'quit' to exit): ")
        if user_question.lower() == 'quit':
            print("Come back soon!")
            break
        else:
            print(random.choice(responses))


magic_8_ball()


'''
Task 3: The Card Picker
Develop a game where the computer randomly picks a card from a deck, and the player has to guess the suit or the rank. Use random.choice() 
to select the card, and then check if the player's guess matches the suit or rank of the chosen card.
'''


import random

def secret_card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return random.choice(deck)

def guess_the_card():
    secret = secret_card()
    print("Welcome to the Guess that Card game! What card did I pick? ")

    while True:
        guess = input("Enter your guess (or type 'quit' to exit): ").strip().lower()
        
        if guess == 'quit':
            print("Goodbye!")
            break
        elif guess in secret:
            print("Congratulations! You've guessed the correct card!")
            break
        else:
            print("Your guess is incorrect. Try again.")

# Start the game
guess_the_card()

'''
Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, each with its
unique style and purpose. By the end of this assignment, you will be able to control your loops like a DJ controls the tracks, ensuring each element gets its time to shine.
Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter 
that displays the number of the track before the genre.
'''
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

genre_message = {
    "Jazz": "Smooth and easy listening",
    "Rock": "Get pumped up!",
    "Hip-hop": "Ride the beat!",
    "Classical": "Relax and meditate"
}

# Initialize track number
track_number = 1

# Spinning through the genres
for genre in genres:
    print(f"Track {track_number}: Now playing {genre}, {genre_message}")

'''
Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the 
loop if a certain genre is played.
'''
# Our playlist is still going
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # We start at the first track

# Keep the party alive until we've reached a specific genre
stop_genre = 'Hip-hop'

# Keep the party alive until we've reached the end or the stop_genre
while i < len(genres) and genres[i] != stop_genre:
    print("Remixing: " + genres[i])
    i += 1  # Move to the next track

'''
Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that 
the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show.
'''
# Our playlist needs a light show
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Skip the light show for this genre
    print(f"Track {index + 1}: {genres[index]} - Light show is on!")

'''
Advance your looping skills by exploring more complex list manipulations. You will learn to selectively loop through parts of a 
list, use list comprehensions for concise code, and generate numerical lists with Python's range function.
Task 1: The Selective DJ
Loop through a slice of the genres list and print only the selected genres. Use slicing to create a sublist of genres from the second to the fourth track.
'''
genres = ["Rock", "Classical", "Hip=Hop", "Jazz"] #added list to referncce the given code
# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)


'''
Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.
'''
genre = ["Rock", "Classical", "Hip-Hop", "Jazz"] #missing list to reference given code
# List comprehension to append "Music" to each genre
music_genres = [genre + " Music" for genre in genre]
print(music_genres)


'''
Task 3: Numerical Beats with range
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".
'''
# Countdown with range
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")
