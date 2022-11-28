# -*- coding: utf-8 -*-
"""
Program: Assignment 01
Author: Paolo
Last date modified: 2022/09/11

"""

## question 03

### Variables
# Message to be displayed at the start
user_message = 'Please enter 2 numbers: '

### receive input
# read user input & store in variables
user_input_1 = input(user_message)
user_input_2 = input(user_message)

### Logic
# cast input from text to number
number_1 = int(user_input_1)
number_2 = int(user_input_2)

# perform the calculation: Substraction of the numbers
result = number_1 - number_2

### Print the result to the screen
print("Substraction of 2 numbers is: ", result)
