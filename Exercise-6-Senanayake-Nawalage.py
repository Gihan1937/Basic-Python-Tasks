# -*- coding: utf-8 -*-
"""
Program: Assignment 01
Author: Paolo
Last date modified: 2022/09/11

"""

## question 06

### libraries ###
# import the math library
from math import *

### Variables
# Message to be displayed at the start
user_message = 'Please enter side Size of the Square: '

### receive input
# read user input & store in variables
user_input_1 = input(user_message)


### Logic
# cast input from text to number
number_1 = float(user_input_1)


# perform the calculation: calculate the are of the Square
result = pow(number_1,2)


### Print the result to the screen
print("Area of the Square is: ", result)
