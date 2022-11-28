# -*- coding: utf-8 -*-
"""
Program: Assignment 01
Author: Paolo
Last date modified: 2022/09/11

"""

## question 08

### libraries ###
# import the math library
from math import *

### Variables
# Message to be displayed at the start
user_message_1 = 'Please enter base size of the Triangle: '
user_message_2 = 'Please enter height size of the Triangle: '

### receive input
# read user input & store in variables
user_input_1 = input(user_message_1)
user_input_2 = input(user_message_2)

### Logic
# cast input from text to number
number_1 = int(user_input_1)
number_2 = int(user_input_2)

# perform the calculation: calculate the are of the Triangle
result = (number_1 * number_2)/2


### Print the result to the screen
print("Area of the Triangle is: ", result)

