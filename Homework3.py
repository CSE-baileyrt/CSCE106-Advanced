# The purpose of this assignment is to demonstrate mastery of creating and calling functions

# In Lecture 4, we wrote a very simple calculator together. You will expand that calculator.
# Instructions:
# 1. Allow the user to enter decimal numbers (not just integers)
# 2. Create more functions to perform math operations
#       This program will be able to perform 8 total functions
#       NOTE: Some math functions do not allow decimal numbers. If that is the case, print a warning to the user
#           that their input (entered as a decimal) has been altered. No suprises! 
# 3. Alter the "calculate" function to pass the function call through to the math operation
# 4. Alter the user interaction section to allow the user to perform as many calculations as they wish
#       Any looping structure is acceptable
#       Also display the 4 new calculation options

# imports section
import math

# functions section
# TODO 2: add 4 more functions of your design
# TODO 2: convert to int numbers if needed (if the function cannot handle decimals)
def add_nums(a, b):
    return a + b
def sub_nums(a, b):
    return a - b
def mul_nums(a, b):
    return a * b
def div_nums(a, b):
    return a / b

def calculate(a, b, oper):
    if oper=='a':
        print("the sum is {}".format(add_nums(a, b)))
    elif oper=='s':
        print("the difference is {}".format(sub_nums(a, b)))
    elif oper=='m':
        print("the product is {}".format(mul_nums(a, b)))
    elif oper=='d':
        print("the quotient is {}".format(div_nums(a, b)))
    # TODO 3: add more calculate handlers
    else:
        print("invalid operation")

# user interactions section
# TODO 4: add a loop
# TODO 1: allow decimal inputs
u_a = int(input("Enter a number: "))
u_b = int(input("Enter a second number: "))
# TODO 4: alter the menu
u_oper = input("Select an operation: a) add, s) subtract, m) multiply, d) divide: ")
calculate(u_a, u_b, u_oper)