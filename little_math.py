""" 
Prompts the user for a level, n. 
If the user does not input 1, 2, 3, 4 or 5, the program should prompt again.
Randomly generates ten (5) math problems formatted as X + Y = , 
wherein each of X and Y is a non-negative integer with n digits.
Prompts the user to solve each of those problems. 
If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, 
allowing the user up to three tries in total for that problem. 
If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 5.
 """
 # import libraries
import random

# let the user set the level 1-5
def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level in (1,2,3,4,5):
                return level
            else:
                raise ValueError
        except ValueError:
            continue

get_level()