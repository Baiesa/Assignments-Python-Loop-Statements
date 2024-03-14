'''
Task 1: 
Code Correction
The code below is intended to print a 3x3 grid of asterisks. 
However, the current output is not as expected. 
Identify the logical errors in the nested loops and correct the code so that it prints the grid correctly, 
with each row of asterisks on a new line.

'''


# for i in range(3):
#     for j in range(3):
#         print("*", end=" ")
#     print()


'''
Task 2: 
Your Mood Tracker
Simulate a mood tracker that records your mood at three 
different times of the day (morning, afternoon, evening) for each day of the week. 
Use nested loops to implement this: the outer loop should iterate over the days, 
and the inner loop should iterate over the times of the day. For each time, 
randomly select a mood from a predefined list and print it.

'''
# import random

# times_of_the_day = ["morning", "afternoon", "evening"]
# days_of_week = ["saturday", " sunday", "monday", "tuesday", "wendsday", "thursday", "friday"]
# moods = ["happy", "sad", "energitic", "calm"]

# for day in days_of_week:
#     print(f"mood tracker for {day}:")
#     for time in times_of_the_day:
#          mood = random.choice(moods)
#          print(f"{time}: {mood}")
# print()

'''
Task 3: 
Multiplication Table
Your task is to create a multiplication table for numbers 1 through 5. 
Use nested loops where the outer loop represents the multiplier 
and the inner loop represents the multiplicand. Print the results in a tabular format.

'''
# multipliers = range(1, 6)
# multiplicands = range(1, 6)

# print("Multiplication Table:")
# print("   |", end="")
# for multiplicand in multiplicands:
#     print(f"  {multiplicand}", end="")
# print("\n---|------------------")
# for multiplier in multipliers:
#     print(f"{multiplier:2} |", end="")
#     for multiplicand in multiplicands:
#         product = multiplier * multiplicand
#         print(f" {product:2}", end="")
#     print()



