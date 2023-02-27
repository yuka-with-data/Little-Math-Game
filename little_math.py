""" 

 """
 # import libraries
import random

# let the user set the level 1-5
def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level = (1,2,3,4,5):
                return level
            else:
                raise ValueError
        except ValueError:
            continue