'''
Task 1: 
Random Choice Game
Create a game where a player has to guess the random item picked by the computer from a list. 
Use random.choice() to select the item and take the user's guess via input. 
Provide feedback on whether they guessed correctly or not.

'''
import random
computer = input("choose an items. ")
lists_of_items = ["action", "fight", "running", "jumping"]
while True:
    computer = input("choose an items. ")
    games = random.choice(lists_of_items)
    if computer == games:
        print("you guess correctly")
        break
    else:   
        print("sorry try again later")




