""" 
Multiplicatin Practice Game
The user chooses the multiplicatin level they want to practice.
10 random questions are generated, and the user has 2 chances to answer correctly.
The user gets 1 point every time they answer correctly.
The max possible score is 10. 
 """

import random
from operator import mul

class MultipleGenerator():
    def __init__(self):
        self.level = self.get_level()
        self.score = 0
        self.prev_y = []
    
    def __str__(self):
        return f'Final Score is {self.score}/10. Great Job!'
    
    """ 
     level decorators: property and setter for level attribute allows us to
     get and set the level value from outside the Class.
       """
    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        if value not in range(1,13):
            raise ValueError
        self._level = value

    """ 
     score decorators: property and setter for score attribute allows us to 
     get and set the score value from outside the Class.
       """
    @property
    def score(self) -> int:
        return self.__score
    
    @score.setter
    def score(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        if value < 0 or value > 10:
            raise ValueError
        self.__score = value

    """ 
     getter property for prev_y attribute allows us to get the list of
     perviously generated values from outside the Class.
       """
    def prev_y(self) -> list[int]:
        return self._prev_y
    
    """ 
     Class Methods
       """
    def get_level(self) -> int:
        while True:
            try:
                level = int(input("Level: "))
                self.level = level
                return self.level
            except ValueError:
                print("Invalid input. Enter a number between 1 and 12.")
    
    def generate_int(self) -> int:
        while True:
            Y = random.randrange(1,13)
            if Y not in self.prev_y:
                self.prev_y.append(Y)
                return Y
    
    def multi_prob(self) -> int:
        for _ in range(10):
            X, Y = self.level, self.generate_int()
            # user gets 2 chances to answer correctly
            for _ in range(2):
                try:
                    ans_input = int(input(f"{X} * {Y} = "))
                except ValueError:
                    print("Enter a valid integer")
                    continue
                if ans_input == mul(X,Y):
                    self.score += 1
                    break
                else:
                    print("wrong answer...")
            else:
                print(f"The correct answer is {mul(X,Y)}")
        return self.score

""" 
Call main function to create instance of Class, and execute main math game function.
 """
def main():
    # create an instance of Class and assign to the variable
    multi = MultipleGenerator()
    # call multi_prob function to generate math game
    multi.multi_prob()
    # print __str__ in the Class
    print(str(multi))

if __name__ == "__main__":
    main()