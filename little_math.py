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

Class:
level
operator
X
Y

decorators
set X is grater than Y
set decimal place, 2

Error Handlings

 """
 # import libraries
import random
from operator import add, sub, mul, truediv

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

# let user pick order of operation
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
            return operator, operator_mapping[operator]
        else:
            continue

def generate_int(level: int) -> int:
    if level == 1:
        return random.randrange(10**(level-1)-1,10**level)
    else:
        return random.randrange(10**(level-1),10**level)

def math_prob(level: int, op_symbol: str, op_func: callable):
    # score tracking    
    score = 0
    # ask user 5 unique question
    for _ in range(5):
        X, Y = generate_int(level), generate_int(level)
        # user gets 3 chances to answer correctly
        for _ in range(3):
            ans_input = input(f"{X} {op_symbol} {Y} = ")
            if not ans_input.isdigit():
                print("Try Again.")
                continue
            if int(ans_input) == op_func(X,Y):
                score += 1
                break
            else:
                print("wrong answer... Try again.")
        else:
            print(f"The answer is {op_func(X,Y)}")
    return score

def main():
    #level = get_level()
    operator_symb, operator_func = get_operator()
    score = math_prob(get_level(), operator_symb, operator_func)
    print(f"Your score is {score}/5. Great Job!")

if __name__ == "__main__":
    main()