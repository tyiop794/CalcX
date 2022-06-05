
import math
from tokenize import Exponent

"""
Ideas:
Ask for operation
Ask for number(s)
Ask how many numbers?
Perform operation on numbers
Type '?' (or '0') to determine additional functionality (scientific calculator)
Ability to define different calculator functions with a command
Save answer from previous operation as 'Ans'; can be pulled when needed
Accept both decimal and integer numbers
reload menu until correct operation is specified ('while' loop)
error handling: check if user types in integer; if user does not, error out with proper message
put all possible operations into an array for easier access
allow user to add function(s) without having to edit the code
specify different operation for each number; do not restrict to one operator
allow functions to be run independent of the total; ask whether final should be added to / saved as total
Error handling: handle errors if string is typed in instead of integer; do not let program crash
Ask for operation after each number typed; after another number is typed, show total before asking for another operation
--> Default operation should be the same one; should user not enter anything, the operation will be the same as that previously used
Add operators (functions) into array and access array when accessing function; avoid using so many if/else statements
Save previous answers / totals into array for later use (add as additional operator)
Make interface?
Specify degree to which number should be rounded (default to the hundreds place)

GUI version:
- becomes primary area for functions, both basic and scientific
"""

def add(old_num, num):
    new_num = old_num + num
    return new_num

def multiply(old_num, mult_num):
    new_num = old_num * mult_num
    return new_num 

def subtract(old_num, sub_num):
    new_num = old_num - sub_num
    return new_num

def divide_decimal(old_num, divisor):
    new_num = (old_num / divisor)
    return new_num
     
def sqroot(num):
    new_num = math.sqrt(num)
    return new_num

def ln(num):
    new_num = math.log(num)
    return new_num

def log_ten(num):
    new_num = math.log(num, 10)
    return new_num

def num_sqrd(num):
    new_num = num ** 2
    return new_num

def num_exp(num, exp):
    new_num = num ** exp
    return new_num

def pi():
    new_num = math.pi
    return new_num

def num_root(num, root_num):
    new_num = num ** (1/root_num)
    return new_num

def sin(num):
    new_num = math.sin(num)
    return new_num

def ee(num, scnd_num):
    new_num = num * (10 ** scnd_num)
    return new_num

def cos(num):
    new_num = math.cos(num)
    return new_num

