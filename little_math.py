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


What I am working on next:

Error Handlings
Decorators

 """
# import libraries
import random
from operator import add, sub, mul, truediv

class MathGame:
    def __init__(self, level=1):
        self.level = level
        self.score = 0
        self.op_symbol = ""
        self.op_func = None
        """ 
         op_symbol and op_func are initialized to empty string and 'None'
         because they are not known yet until the user provides valid input.
           """

    def __str__(self):
        return f"Your Final Score is {self.score} out of 5. Great Job!"
    
    # handle errors - LEVEL
    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        self._level = value

    @property
    def score(self) -> int:
        return self.__score
    
    @score.setter
    def score(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        if value < 0 or value > 5:
            raise ValueError
        self.__score = value

    @staticmethod
    def get_level() -> int:
        while True:
            try:
                level = int(input("Level: "))
                if level not in (1,2,3):
                    raise ValueError
                return level
            except ValueError as e:
                print(e,"Invalid level. Try again.")
                continue

    @staticmethod
    def get_operator() -> tuple[str, callable]:
        operator_mapping = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv
        }
        while True:
            operator = input("Operator: ")
            if operator in operator_mapping:
                op_func = operator_mapping[operator]
                print(f"Debug: operator {operator} with function {op_func}")
                return operator, op_func
            else:
                print("Invalid operator. Try again.")
                continue
    
    def generate_int(self) -> int:
        if self.level == 1:
            """ 
             When the level is 1, set the range between 1 and 10,
             to prevent Zero Division Error from happening.
               """
            return random.randrange(10**(self.level-1),10**self.level)
        else:
            return random.randrange(10**(self.level-1),10**self.level)

    def math_prob(self) -> int:
        # get operator
        self.op_symbol, self.op_func = self.get_operator()
        # ask user 5 unique question
        for _ in range(5):
            X, Y = self.generate_int(), self.generate_int()
            # Set X is always grater than Y
            if X < Y:
                X, Y = Y, X
            # user gets 2 chances to answer correctly
            for _ in range(2):
                ans_input = input(f"{X} {self.op_symbol} {Y} = ")
                try:
                    ans_float = round(float(ans_input), 1)
                except ValueError:
                    print("Input has to be in digit. Try Again.")
                    continue

                answer = round(float(self.op_func(X,Y)),1)

                if ans_float == answer:
                    self.score += 1
                    break
                else:
                    print("wrong answer... Try again.")
            else:
                print(f"The answer is {answer}")
        return self.score

# main function
def main():
    level = MathGame.get_level()
    game = MathGame(level=level)
    game.math_prob()
    print(str(game))

if __name__ == "__main__":
    main()