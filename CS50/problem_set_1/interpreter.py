#! /usr/bin/python3
"""
File:   extensions.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In a file called interpreter.py, implement a program that prompts the user for an
    arithmetic expression and then calculates and outputs the result as a floating-point
    value formatted to one decimal place. Assume that the user’s input will be formatted
    as x y z, with one space between x and y and one space between y and z, wherein:
        - x is an int
        - y is [+, -, *, /]
        - z is an int

Info:
    https://cs50.harvard.edu/python/psets/1/interpreter/

"""

#
# Globals
#
math_symbols = ["+", "-", "*", "/"]


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # get expression from user
    user_expression = input("Expression: ")

    # process expression
    process_expression(user_expression)


def process_expression(exp):
    """
    Implement logic
    """
    # get incredients
    x, y, z = exp.split(" ")

    # str to integer conversion
    x_int = int(x)
    z_int = int(z)

    # calculate
    match y:
        case str if math_symbols[0] in str:
            res = x_int + z_int
            print(float(res))
        case str if math_symbols[1] in str:
            res = x_int - z_int
            print(float(res))
        case str if math_symbols[2] in str:
            res = x_int * z_int
            print(float(res))
        case str if math_symbols[3] in str:
            res = x_int / z_int
            print(float(res))


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
